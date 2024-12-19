import re
import copy

sum = 0
with open("data.txt") as file:
    for i, row in enumerate(file):
        digits = re.findall("\d+", row)
        control = digits[0]
        digits.pop(0)
        print("row:", i)
        
        # print(digits)
        # print(control)
        
        comb = []
        for digit in digits:
            # print("digit", digit)
            if len(comb) == 0:
                comb.append(int(digit))
                continue
            prev_comb = copy.deepcopy(comb)
            # if len(comb) > 1:
                # comb.pop(0)
            list1 = copy.deepcopy(comb)
            for el in list1:
                addition = int(digit) + int(el)
                multiplication = int(digit) * int(el)
                concatination = int(str(el) + str(digit)) # concatinate
                
                if not addition > int(control):
                    comb.append(addition)
                if not multiplication > int(control):
                    comb.append(multiplication)
                if not concatination > int(control):
                    comb.append(concatination)
            new_comb = [x for x in comb if x not in prev_comb]
            comb = new_comb
            # print("TEST", comb)
            
        
        if comb.count(int(control)) > 0:
            sum += int(control)
        # print(comb)
        # break
        # for i in range((len(digits) - 1)*2):
            
print(sum)
# print(81 + 40 * 27)
            
            
# with open("data.txt") as file:
#     for y, row in enumerate(file):
#         group = []
#         for x, char in enumerate(row.strip()):