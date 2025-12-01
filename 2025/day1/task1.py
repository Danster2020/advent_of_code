list = []
with open("puzzle_ex.txt") as file:
    for row in file:
        list.append(row.strip())

def rotate(curr_val: int, input: str):
    letter = input[0]
    value = int(input[1:])
    
    calc = -1
    if letter == "R":
        calc = curr_val + value
    else:
        calc = curr_val - value
    
    return calc % 100

amt_of_zeros = 0
start_val = 50
for value in list:
    start_val = rotate(start_val, value)
    if start_val == 0:
        amt_of_zeros += 1
    
print(amt_of_zeros)