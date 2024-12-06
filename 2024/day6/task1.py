global list1
global guard_pos_x
global guard_pos_y
global guard_dir
global guard_loc
global counter

list1 = []
guard_pos_x = 0
guard_pos_y = 0
guard_dir = "UP"
guard_loc = []
counter = 0

def print_map(my_list):
    for row in my_list:
        print(row)

def turn_right():
    global list1
    global guard_pos_x
    global guard_pos_y
    global guard_dir
    global guard_loc
    
    print("turned right")
    
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
    global guard_loc
    
    keep_walking = True
    
    old_guard_x = guard_pos_x
    old_guard_y = guard_pos_y
    
    # print("guard_dir", guard_dir)
    
    if guard_dir == "UP":
        if new_map[guard_pos_y-1][guard_pos_x] == "#":
            turn_right()
            return True
        guard_pos_y -= 1
        if guard_pos_y == 0:
            keep_walking = False
    elif guard_dir == "DOWN":
        if new_map[guard_pos_y+1][guard_pos_x] == "#":
            turn_right()
            return True
        guard_pos_y += 1
        if guard_pos_y == len(list1):
            keep_walking = False
    elif guard_dir  == "RIGHT":
        if new_map[guard_pos_y][guard_pos_x+1] == "#":
            turn_right()
            return True
        if guard_pos_x == len(list1[0]):
            keep_walking = False
        guard_pos_x += 1
    elif guard_dir == "LEFT":
        print("ADFAFSF")
        if new_map[guard_pos_y][guard_pos_x-1] == "#":
            turn_right()
            return True
        guard_pos_x -= 1
        if guard_pos_x == 0:
            keep_walking = False
    
    # if (guard_pos_x < 0 or guard_pos_y < 0) or (guard_pos_x > len(list1)-1 or guard_pos_y > len(list1[0])-1):
    #     return False
    
    
    
    icon = new_map[old_guard_y][old_guard_x]
    # print("TEST", icon)
    new_map[old_guard_y][old_guard_x] = "X"
    # print("guard_pos_x", guard_pos_x, "guard_pos_y", guard_pos_y)
    new_map[guard_pos_y][guard_pos_x] = icon
    
    
    return keep_walking
    
def main():
    global list1
    global guard_pos_x
    global guard_pos_y
    global guard_dir
    global guard_loc
    global new_map
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
                    guard_loc.append(group2)
                group.append(char)
            list1.append(group)
    # print_map(list1)

    new_map = list1.copy()
    # print("TEST1", new_map[guard_pos_x][guard_pos_y])

    leaving = False
    while not leaving:
        print(guard_pos_x, guard_pos_y)
        if not walk_forward():
            leaving = True
            break
        # print_map(new_map)
            
    print("guard_pos_x", guard_pos_x, "guard_pos_y", guard_pos_y)
    print(guard_loc)
    print_map(new_map)
    print("DONE")
    
    global counter
    
    for row in list1:
        for col in row:
            if col == "X":
                counter += 1
    
    print(counter + 1)  

main()