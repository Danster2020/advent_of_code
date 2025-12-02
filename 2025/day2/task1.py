puzzle_list = []
with open("puzzle.txt", encoding="utf-8") as file:
    for row in file:
        puzzle_list.append(row.strip())

interval_list = puzzle_list[0].split(",")
numbers_list = []
for interval in interval_list:
    numbers_list.append(interval.split("-"))

# print(numbers_list)

def get_invalid_ids(start_stop_list):
    invalid_ids = []
    start_val = (start_stop_list[0])
    stop_val = (start_stop_list[1])
    
    curr_val = start_val
    for val in range(int(start_val), int(stop_val) +1):
        curr_val = str(val)
        # skip if length of val is uneven
        if len(curr_val) % 2 != 0:
            continue
        first_half, second_half = curr_val[:len(curr_val)//2], curr_val[len(curr_val)//2:]
        # print("TEST", first_half, second_half)
        if first_half == second_half:
            invalid_ids.append(val)
    
    # print(start_val, stop_val)
    return invalid_ids

all_invalid_ids = []
for element in numbers_list:
    all_invalid_ids.append(get_invalid_ids(element))

sum_of_all_invalid_ids = 0
# all_invalid_ids = get_invalid_ids(numbers_list[1])
for val_range in all_invalid_ids:
    for value in val_range:
        sum_of_all_invalid_ids += value

# print(all_invalid_ids)
print("sum:", sum_of_all_invalid_ids)