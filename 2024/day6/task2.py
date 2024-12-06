from asyncio import sleep
import copy


global list1
global guard_pos_x
global guard_pos_y
global guard_dir
global guard_loc_history
global loops
global nr_of_loops

list1 = []
guard_pos_x = 0
guard_pos_y = 0
guard_dir = "UP"
guard_loc_history = []
loops = 0
nr_of_loops = 0

def print_map(my_list):
    for row in my_list:
        print(row)

def turn_right():
    global list1
    global guard_pos_x
    global guard_pos_y
    global guard_dir
    global guard_loc_history
    global loops
    
    group1 = []
    group1.append(guard_pos_x)
    group1.append(guard_pos_y)
    
    if len(guard_loc_history) == 0:
        guard_loc_history.append(tuple(group1))
    elif (tuple(group1) != guard_loc_history[-1]):
        guard_loc_history.append(tuple(group1))
    
    if len(guard_loc_history) != len(set(guard_loc_history)):
        loops = 2
        return
    
    if guard_dir == "UP":
        guard_dir = "RIGHT"
        new_map[guard_pos_y][guard_pos_x] = ">"
    elif guard_dir == "RIGHT":
        guard_dir = "DOWN"
        new_map[guard_pos_y][guard_pos_x] = "v"
    elif guard_dir == "DOWN":
        guard_dir = "LEFT"
        new_map[guard_pos_y][guard_pos_x] = "<"
    elif guard_dir == "LEFT":
        guard_dir = "UP"
        new_map[guard_pos_y][guard_pos_x] = "^"
        
def walk_forward():
    global list1
    global guard_pos_x
    global guard_pos_y
    global guard_dir
    global guard_loc_history
    global loops
    
    keep_walking = True
    old_guard_x = guard_pos_x
    old_guard_y = guard_pos_y
    
    if guard_dir == "UP":
        pos = new_map[guard_pos_y-1][guard_pos_x]
        if pos == "#" or pos == "O":
            turn_right()
            return True
        guard_pos_y -= 1
        if guard_pos_y == 0:
            keep_walking = False
    elif guard_dir == "DOWN":
        pos = new_map[guard_pos_y+1][guard_pos_x]
        if pos == "#" or pos == "O":
            turn_right()
            return True
        guard_pos_y += 1
        if guard_pos_y == len(list1):
            keep_walking = False
    elif guard_dir  == "RIGHT":
        pos = new_map[guard_pos_y][guard_pos_x+1]
        if pos == "#" or pos == "O":
            turn_right()
            return True
        if guard_pos_x == len(list1[0]):
            keep_walking = False
        guard_pos_x += 1
    elif guard_dir == "LEFT":
        pos = new_map[guard_pos_y][guard_pos_x-1]
        if pos == "#" or pos == "O":
            turn_right()
            return True
        guard_pos_x -= 1
        if guard_pos_x == 0:
            keep_walking = False
    
    
    icon = new_map[old_guard_y][old_guard_x]
    new_map[old_guard_y][old_guard_x] = "X"
    new_map[guard_pos_y][guard_pos_x] = icon
    
    return keep_walking
    
def main():
    global list1
    global guard_pos_x
    global guard_pos_y
    global guard_dir
    global guard_loc_history
    global new_map
    global loops
    global nr_of_loops
    
    with open("data.txt") as file:
        for y, row in enumerate(file):
            group = []
            for x, char in enumerate(row.strip()):
                if char == "^":
                    guard_pos_x = x
                    guard_pos_y = y
                    group2 = []
                    group2.append(x)
                    group2.append(y)
                group.append(char)
            list1.append(group)

    org_guard_pos_x = guard_pos_x
    org_guard_pos_y = guard_pos_y

    for i in range(len(list1)):
        for j in range(len(list1[0])):
            guard_loc_history = []
            guard_pos_x = org_guard_pos_x
            guard_pos_y = org_guard_pos_y
            guard_dir = "UP"
            loops = 0
            print("ij", i, j)
            new_map = copy.deepcopy(list1)
            if list1[i][j] != "^" and list1[i][j] != "#":
                new_map[i][j] = "O"
            else:
                continue
            
            leaving = False
            while not leaving:
                
                if guard_pos_y == len(list1) -1 or guard_pos_x == len(list1[0]) -1:
                    leaving = True
                    break
                
                if not walk_forward():
                    leaving = True
                    break

                if loops > 1:
                    nr_of_loops += 1
                    loops = 0
                    leaving = True
                    break
                    
    print(nr_of_loops)

main()