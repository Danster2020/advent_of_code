import collections
import re

rules = []
prints = []
dict1 = collections.defaultdict(list)

rules_done = False
with open("data.txt") as file:
    for row in file:
        row_string = row.strip()
        if row_string == "":
            rules_done = True
            continue
        elif not rules_done:
            rule = re.findall("\d+", row_string)
            dict1[rule[1]].append(rule[0])
            rules.append(re.findall("\d+", row_string))
        else:
            prints.append(re.findall("\d+", row_string))
# print(rules)
print(prints)
# print(dict1)

middle_page_sum = 0
for print_out in prints:
    valid_print_out = True
    
    for i in range(len(print_out)):
        number = print_out[i]
        
        for rule in dict1[number]:
            try:
                print("TEST", print_out.index(rule))
                if print_out.index(rule) > i:
                    valid_print_out = False
                    break
            except ValueError as e:
                pass
    if valid_print_out:
        middle_page_sum += int(print_out[int((len(print_out) - 1) / 2)])

print(middle_page_sum)