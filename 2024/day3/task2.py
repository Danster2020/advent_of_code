import re

list = []
with open("data.txt") as file:
    for row in file:
        regex = re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)", row)
        list.append(regex)

enabled = True
result = 0
for row in list:
    for value in row:
        if value == "don't()":
            enabled = False
        elif value == "do()":
            enabled = True
        elif enabled == True:
            arg_list = re.findall("\d+", value)
            result += int(arg_list[0]) * int(arg_list[1])

print(result)