import re

list1 = []
with open("data.txt") as file:
    for row in file:
        group = []
        for char in row.strip():
            group.append(char)
        list1.append(group)

nr_of_xmas = 0
regex_1 = "MAS"
regex_2 = "SAM"

for row in range(len(list1) - 2):
    for col in range(len(list1[0]) - 2 ):
        tl = list1[row][col]
        tr = list1[row][col + 2]
        mi = list1[row + 1][col + 1]
        bl = list1[row + 2][col]
        br = list1[row + 2][col + 2]
        
        diag_1 = len(re.findall(regex_1, tl + mi + br)) + len(re.findall(regex_2, tl + mi + br))
        diag_2 = len(re.findall(regex_1, bl + mi + tr)) + len(re.findall(regex_2, bl + mi + tr))
        if diag_1 + diag_2 == 2:
            nr_of_xmas += 1

print(nr_of_xmas)