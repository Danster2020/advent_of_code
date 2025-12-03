puzzle_list = []
with open("puzzle.txt", encoding="utf-8") as file:
    for row in file:
        puzzle_list.append(row.strip())
    
joltage_sum = 0
for battery in puzzle_list:
    max_digit_1 = 0
    max_digit_1_pos = 0
    max_digit_2 = 0
    
    for i, digit in enumerate(battery):
        if int(digit) > max_digit_1 and i < len(battery) - 1:
            max_digit_1 = int(digit)
            max_digit_1_pos = i
    
    for i, digit in enumerate(battery):
        if int(digit) > max_digit_2 and i > max_digit_1_pos:
            max_digit_2 = int(digit)
    
    joltage_sum += int(str(max_digit_1) + str(max_digit_2))
    
print("joltage_sum", joltage_sum)
    