left_list = []
right_list = []

with open("data.txt") as file:
    for row in file:
        values_list = row.split()
        left_list.append(int(values_list[0]))
        right_list.append(int(values_list[1]))
        
left_list.sort()
right_list.sort()
total_delta_value = 0

for i in range(len(left_list)):
    total_delta_value += abs(left_list[i] - right_list[i])

print(total_delta_value)