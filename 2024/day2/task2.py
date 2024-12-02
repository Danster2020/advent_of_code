list = []
with open("data.txt") as file:
    for row in file:
        values_list = row.split()
        values_list = [int(element) for element in values_list]
        list.append(values_list)
nr_of_safe = 0

# for every row
for i in range(len(list)):
    nr_of_unsafe = 0
    
    unsafe_list = [1] * len(list[i])
    
    # for every combination in row
    for combination in range(len(list[i])):
        temp_list = list[i].copy()
        direction = 0
        del temp_list[combination]
        
        # for every element
        for j in range(len(temp_list) - 1):
            
            curr = temp_list[j]
            next = temp_list[j+1]
            
            delta = next - curr
            
            if delta < 0 and direction == 0:
                direction = -1
            elif delta > 0 and direction == 0:
                direction = 1
                
            if abs(delta) > 3: # difference bigger than 3
                unsafe_list[combination] += 1
                continue
            elif curr == next:
                unsafe_list[combination] += 1
                continue
            if (delta < 0) and direction == 1 or (delta > 0) and direction == -1:
                unsafe_list[combination] += 1
                continue
    for el in unsafe_list:
        if el < 2:
            nr_of_safe += 1
            break
            
print(nr_of_safe)