import collections
import copy
import re


dict1 = collections.defaultdict(list)
map1 = []
unique_sum = 0

def print_map(my_list):
    for row in my_list:
        for char in row:
            print(char, end="")
        print()
    print()
        

with open("data.txt") as file:
    for i, row in enumerate(file):
        row_group = [] 
        for j, col in enumerate(row):
            row_group.append(col.strip())
            station = re.match("\d|[a-zA-Z]", col)
            if station:
                group1 = []
                group1.append(i)
                group1.append(j)
                dict1[station.group(0)].append(group1)
        map1.append(row_group)

map2 = copy.deepcopy(map1)

print(dict1)
# print(map1)

for i, key in enumerate(dict1):
    # print(len(list(dict1.items())[i]) -1)
    for j in range(len(dict1.get(key))):
        # print("LENGTH", len(dict1.get(key)))
        stations = dict1.get(key)
        n_row = stations[j][0]
        n_col = stations[j][1]
        print("n", n_row, n_col)
        
        
        comp_stations = copy.deepcopy(stations)
        comp_stations.pop(j)
        # print("comp", comp_stations)
        
        for k in range(len(dict1.get(key)) -1):
            delta_row = n_row - comp_stations[k][0]
            delta_col = n_col - comp_stations[k][1]
            
            anti_n_row = n_row + delta_row
            anti_n_col = n_col + delta_col
            
            anti_n2_row = comp_stations[k][0] - delta_row
            anti_n2_col = comp_stations[k][1] - delta_col
            
            print(comp_stations)
            print("ego TEST:", n_row, n_col)
            
            if (anti_n_row > -1 and anti_n_col > -1 and anti_n_row < (len(map1)) and anti_n_col < (len(map1[0])-1)):
                try:
                    map2[anti_n_row][anti_n_col] = "#"
                    print("# at:",anti_n_row, anti_n_col)
                    print("debug1:", "ego:", n_row, n_col, "comp:", comp_stations[k][0], comp_stations[k][1])
                except IndexError:
                    pass
            
            if (anti_n2_row > -1 and anti_n2_col > -1 and anti_n2_row < (len(map1)) and anti_n2_col < (len(map1[0])-1)):
                try:
                    map2[anti_n2_row][anti_n2_col] = "#"
                    print("# at:",anti_n2_row, anti_n2_col)
                    print("debug2:", "ego:", n_row, n_col, "comp:", comp_stations[k][0], comp_stations[k][1])
                except IndexError:
                    pass
            
            print_map(map2)
        
            # print(anti_n_row, anti_n_col)
            # print(anti_n2_row, anti_n2_col)

# print_map(map2)
for row in map2:
    for col in row:
        match = re.findall("#", col)
        unique_sum += len(match)
    
print(unique_sum)