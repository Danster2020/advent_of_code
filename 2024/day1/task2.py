left_list = []
right_list = []

with open("data.txt") as file:
    for row in file:
        values_list = row.split()
        left_list.append(int(values_list[0]))
        right_list.append(int(values_list[1]))
        
left_list.sort()
right_list.sort()
total_similarity = 0

for i in range(len(left_list)):
    occurence = 0
    for right_value in right_list:
        if left_list[i] == right_value:
            occurence += 1
    total_similarity += left_list[i] * occurence

print(total_similarity)