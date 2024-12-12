
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

stack1 = []
for char in list1:
    if char != ".":
        stack1.append(char)

list2 = copy.deepcopy(list1)
for i, char in enumerate((list1)):
    if char == ".":
        
        # check if sort complete
        string1 = "".join(map(str, list2))
        if len(re.findall("\d+", string1)) == 1:
            break
        
        right_el = stack1.pop()
        print(len(stack1))
        for li_index, value in reversed(list(enumerate(list2))):
            if value != ".":
                list2.pop(li_index)
                break
                
        if right_el == ".":
            list2.append(".")
            continue
        else:
            for j in range (len(list2)):
                el = list2[j]
                if el == ".":
                    list2[j] = right_el
                    break
        list2.append(".")
   
print(list2)

checksum = 0
for id, digit in enumerate(list2):
    if digit == ".":
        break
    checksum += id * digit

print(checksum)