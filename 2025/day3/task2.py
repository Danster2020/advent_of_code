puzzle_list = []
with open("puzzle.txt", encoding="utf-8") as file:
    for row in file:
        puzzle_list.append(row.strip())

joltage_sum = 0
for battery in puzzle_list:
    
    max_digit_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    max_digit_pos_list = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    
    # for 12 numbers
    for nr in range(12):
        # for every digit
        for i, digit in enumerate(battery):
            if int(digit) > max_digit_list[nr] and i < len(battery) - 11 + nr and i > max_digit_pos_list[nr-1]:
                max_digit_list[nr] = int(digit)
                max_digit_pos_list[nr] = i
  
    print(max_digit_list, max_digit_pos_list)
    digit_list_to_int = ""
    for digit in max_digit_list:
        digit_list_to_int += str(digit)
    joltage_sum += int(digit_list_to_int)

print(joltage_sum)
