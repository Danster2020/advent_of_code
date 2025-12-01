list = []
with open("puzzle.txt") as file:
    for row in file:
        list.append(row.strip())
print(list)

def rotate(curr_val: int, command: str):
    letter = command[0]
    nr_of_steps = int(command[1:])
    zero_count = 0
    
    operation = None
    if letter == "R":
        operation = 1
    else:
        operation = -1
    
    moving_val = curr_val
    for i in range(nr_of_steps):
        moving_val += operation
        if moving_val == -1:
            moving_val = 99
        if moving_val == 100:
            moving_val = 0
        if moving_val == 0:
            zero_count += 1
            
    # print("curr_val:", curr_val, "input:", command, "zeros_passed:", zero_count)
    
    return (moving_val, zero_count)

zeros_passed = 0
start_val = 50
for value in list:
    start_val, nr_of_zeros = rotate(start_val, value)
    zeros_passed += nr_of_zeros
    
print(zeros_passed)
