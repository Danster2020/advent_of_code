

def calc_value(char):
    ascii_char = ord(char)
    value = 0
    print("ord",ascii_char)
    
    # small letter
    if ascii_char >= 97:
        value = ascii_char - 97 + 1 # ascii + priority
    else:
        value = ascii_char - 65 + 27 # ascii + priority
    return value

with open('data.txt') as f:
    sum_proirity = 0
    for i in range (300):
        comp_1 = []
        comp_2 = []
        line = f.readline()
        length_comp = len(line) - 1 # compensates for newline char
        print(length_comp)
        comp_length = int(length_comp/2)
        for i in range(comp_length):
            comp_1.append(line[i])
            comp_2.append(line[comp_length + i])
        
        for char in comp_1:
            if char in comp_2:
                print("duplicate:",char)
                priority = calc_value(char)
                break
        sum_proirity += priority
            
        
        # print(comp_1)
        # print(comp_2)
print("Total sum:", sum_proirity)