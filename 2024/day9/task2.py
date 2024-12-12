
from collections import OrderedDict, defaultdict
import copy
import re


list1 = []
with open("data.txt") as file:
    for i, row in enumerate(file):
        id = 0
        for pos, digit in enumerate(row):
            increment_id = False
            for times in range(int(digit)):
                if not pos % 2 == 0:
                    list1.append(".")
                else:
                    list1.append(id)
                    increment_id = True
            if increment_id:
                id += 1

print(list1)

files_dict = defaultdict(int)
files_index_dict = defaultdict(list) # id:[startindex, endindex]
free_space_dict = defaultdict(int) # startindex:nr_of_spaces

size_of_free_space = 0
size_of_file = 0
mem_id = None
for i, char in enumerate(list1):
    if char != ".": # if digit
        files_dict[char] += 1
        if size_of_free_space > 0:
            free_space_dict[i-size_of_free_space] = size_of_free_space
            size_of_free_space = 0
        mem_id = char
        size_of_file += 1
    else: # if not digit
        if mem_id != None:
            files_index_dict[mem_id].append(i-size_of_file) # start index
            files_index_dict[mem_id].append(i-1) # end index
            size_of_file = 0
            mem_id = None

        size_of_free_space += 1
    if i == len(list1) - 1 or (list1[i+1] != mem_id and mem_id != None):
        files_index_dict[mem_id].append(i-size_of_file+1) # start index
        files_index_dict[mem_id].append(i) # end index
        size_of_file = 0
        mem_id = None
        

files_dict = dict(sorted(files_dict.items(), reverse=True))


list2 = copy.deepcopy(list1)

def remove_old_id(my_list, index_dict, id):
    start_index = index_dict[id][0]
    end_index = index_dict[id][1]
    for i in range(start_index, end_index + 1):
        my_list[i] = "."
    del index_dict[id]
            

for id, file_size in files_dict.items():
    print(f"{id}")
    removed_old_id = False
    for index, space_size in free_space_dict.items():
        if file_size <= space_size and index < files_index_dict[id][0]:
            new_space_size = space_size - file_size
            del free_space_dict[index]
            free_space_dict[index + file_size] = new_space_size
            free_space_dict = dict(sorted(free_space_dict.items()))
            removed_old_id = True
            for i in range(index, index + file_size):
                list2[i] = id
            break
    
    if removed_old_id:
        remove_old_id(list2, files_index_dict, id)
            
checksum = 0
for id, digit in enumerate(list2):
    if digit != ".":
        checksum += id * digit

print(checksum)