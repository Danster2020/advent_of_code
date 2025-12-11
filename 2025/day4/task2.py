puzzle_list = []
with open("puzzle.txt", encoding="utf-8") as file:
    for row in file:
        row_list = []
        for value in list(row.strip()):
            row_list.append(value)
        puzzle_list.append(row_list)

puzzle_list = tuple(puzzle_list)

def get_neighbors(list: tuple, index: tuple):
    row = index[0]
    col = index[1]
    
    height = len(list)
    width = len(list[0])
    
    neighbor_vals = []
    
    # UL
    if row != 0 and col != 0:
        neighbor_vals.append(list[row - 1][col - 1])

    # U
    if row != 0:
        neighbor_vals.append(list[row - 1][col])
        
    # UR
    if row != 0 and col != width - 1:
        neighbor_vals.append(list[row - 1][col + 1])
        
    # R
    if col != width - 1:
        neighbor_vals.append(list[row][col + 1])
        
    # DR
    if row != height - 1 and col != width - 1:
        neighbor_vals.append(list[row + 1][col + 1])
        
    # D
    if row != height - 1:
        neighbor_vals.append(list[row + 1][col])
        
    # DL
    if row != height - 1 and col != 0:
        neighbor_vals.append(list[row + 1][col - 1])
        
    # L
    if col != 0:
        neighbor_vals.append(list[row][col - 1])

    return neighbor_vals.count("@")


roll_count = 0
modified = True
while modified:
    modified = False
    for i, row in enumerate(puzzle_list):
        for j, col in enumerate(puzzle_list):
            if puzzle_list[i][j] != "." and puzzle_list[i][j] != "x":
                acc_rolls = get_neighbors(puzzle_list, (i, j))
                if acc_rolls < 4:
                    modified = True
                    puzzle_list[i][j] = "x"
                    roll_count += 1
                
print(roll_count)