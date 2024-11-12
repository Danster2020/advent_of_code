#A/X Rock (1p)
#B/Y Paper (2p)
#C/Z Scissors (3p)

# X: loose
# Y: draw
# Z: win

#Points
# lost 0p
# draw 3p
# win 6p

points = 0

def decide_points():
    global points
    points_gained = 0
    
    # move points
    # if "A" in line:
    #     points_gained += 1
    # elif "B" in line:
    #     points_gained += 2
    # elif "C" in line:
    #     points_gained += 3

    # winning conditions
    if ("Z" in line):
        points_gained += 6 # win
        if "A" in line:
            points_gained += 2
        elif "B" in line:
            points_gained += 3
        elif "C" in line:
            points_gained += 1
    # draw conditions
    elif ("Y" in line):
        points_gained += 3 # draw
        if "A" in line:
            points_gained += 1
        elif "B" in line:
            points_gained += 2
        elif "C" in line:
            points_gained += 3
    # losing conditions
    else:
        if "A" in line:
            points_gained += 3
        elif "B" in line:
            points_gained += 1
        elif "C" in line:
            points_gained += 2
    points += points_gained
    print("points gained:", points_gained)


with open('data.txt') as f:
    for i in range (0, 2500, 1): #2500
        line = f.readline()
        # print(line)
        decide_points()
print("Total points:", points)