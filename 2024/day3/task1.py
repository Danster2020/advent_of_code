import re

list = []
with open("data.txt") as file:
    for row in file:
        regex = re.findall("mul\(\d+,\d+\)", row)
        list.append(regex)

result = 0
for row in list:
    for value in row:
        arg_list = re.findall("\d+", value)
        result += int(arg_list[0]) * int(arg_list[1])

print(result)