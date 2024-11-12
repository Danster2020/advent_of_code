#A/X Rock (1p)
#B/Y Paper (2p)
#C/Z Scissors (3p)

#Points
# lost 0p
# draw 3p
# win 6p

points = 0

def decide_points():
    global points
    points_gained = 0
    
    # move points
    if "X" in line:
        points_gained += 1
    elif "Y" in line:
        points_gained += 2
    elif "Z" in line:
        points_gained += 3

    # winning conditions
    if ("X" in line and "C" in line) or \
        ("Y" in line and "A" in line) or \
        ("Z" in line and "B" in line):
        points_gained += 6
    # draw conditions
    elif ("X" in line and "A" in line) or \
        ("Y" in line and "B" in line) or \
        ("Z" in line and "C" in line):
        points_gained += 3
    # losing conditions
    else:
        points_gained += 0
    points += points_gained
    # print("points gained:", points_gained)


with open('data.txt') as f:
    for i in range (0, 2500, 1):
        line = f.readline()
        # print(line)
        decide_points()
print("Total points:", points)