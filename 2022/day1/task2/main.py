elf_food = [0]
elf_id = 0

with open('data.txt') as f:
    for i in range (0, 2243, 1): # 2243
        line = f.readline()
        # print("linedata:", line)
        # print("row:", i)
        if line == "\n":
            elf_id += 1
            elf_food.append(0)
        else:
            elf_food[elf_id] += int(line)
            
elf_food.sort(reverse=True)
print("MAX:", elf_food[0])

sum_top_3 = elf_food[0] + elf_food[1] + elf_food[2]
print("top 3:", sum_top_3)
