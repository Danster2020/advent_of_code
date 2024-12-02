list = []
with open("data.txt") as file:
    for row in file:
        values_list = row.split()
        values_list = [int(element) for element in values_list]
        list.append(values_list)
print(list)
nr_of_safe = 0
for i in range(len(list)):
    direction = 0
    for j in range(len(list[i]) - 1):
        curr = list[i][j]
        next = list[i][j+1]
        delta = curr - next
        if abs(delta) > 3:
            # print("curr", curr)
            # print("next", next)
            # print("delta", delta)
            
            break
        elif curr == next:
            
            break
        if (delta > 0) and direction ==1 or (delta < 0) and direction == -1:
            # print("direction", direction)
            # print("curr", curr)
            # print("next", next)
            # print(i, j, "break")
            
            break
        if (delta) > 0:
            direction = -1
        else:
            direction = 1
        if j == len(list[i]) - 2:
            nr_of_safe += 1
print(nr_of_safe)