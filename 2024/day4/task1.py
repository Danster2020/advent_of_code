import re

list1 = []
with open("data.txt") as file:
    for row in file:
        list1.append(row.strip())

nr_of_xmas = 0
vert_let_string = ""
regex_1 = "XMAS"
regex_2 = "SAMX"

org_size = len(list1)

for row in list1:
    query_1 = re.findall(regex_1, row)
    query_2 = re.findall(regex_2, row)
    nr_of_xmas += len(query_1) + len(query_2) # horisontal

for col in range(len(list1[0])):
    for row in range(len(list1)):
        vert_let_string += list1[row][col]
    
    query_1 = re.findall(regex_1, vert_let_string)
    query_2 = re.findall(regex_2, vert_let_string)
    nr_of_xmas += len(query_1) + len(query_2) # vertical
    vert_let_string = "" # reset string

row_list = [i for i in range(0, len(list1))]
col_list = [i for i in range(0, len(list1))]

diag_1 = [""] * (len(list1) + len(list1[0]) -1)
diag_2 = [""] * (len(list1) + len(list1[0]) -1)

temp_list1 = list1.copy()
temp_list2 = list1.copy()

for i in range(len(temp_list1)):
    temp_list1[i] = list(temp_list1[i])
    temp_list2[i] = list(temp_list2[i])

indent = len(temp_list1) - 1

for row in range(len(temp_list1)):
    for slot in range(indent):
        temp_list1[row].insert(0, "0") # insert 0 at begining
        temp_list2[row].append("0") # insert 0 at end
    if row > 0:
        for i in range(row):
            temp_list1[row].append("0") # insert 0 at end
            temp_list2[row].insert(0, "0") # insert 0 at begining
    indent -= 1
    
for col in range(len(temp_list1[0])):
    for row in range(len(temp_list1)):
        diag_1[col] += temp_list1[row][col]
        diag_2[col] += temp_list2[row][col]
        
for row in range(len(diag_1)):
    pass
    nr_of_xmas += len(re.findall(regex_1, diag_1[row]))
    nr_of_xmas += len(re.findall(regex_2, diag_1[row]))
    
    nr_of_xmas += len(re.findall(regex_1, diag_2[row]))
    nr_of_xmas += len(re.findall(regex_2, diag_2[row]))

print(nr_of_xmas)
