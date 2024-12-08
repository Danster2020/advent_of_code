import re
import copy

sum = 0
with open("data.txt") as file:
    for row in file:
        digits = re.findall("\d+", row)
        control = digits[0]
        digits.pop(0)
        
        comb = []
        for digit in digits:
            if len(comb) == 0:
                comb.append(int(digit))
                continue
            list1 = copy.deepcopy(comb)
            for el in list1:
                comb.append(int(digit) + int(el))
                comb.append(int(digit) * int(el))
        
        if comb.count(int(control)) > 0:
            sum += int(control)
            
print(sum)