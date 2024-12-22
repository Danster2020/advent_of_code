
import collections
import copy
from enum import Enum
import re

class Dir(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Trailwalker:
    
    org_map = []
    trails_to_visit = []
    dirs_to_explore = collections.defaultdict(list)
    curr_pos = (0, 0)
    height = 0
    sum_of_trail_points = 0
    discovered_nines = set()

    
    def __init__(self, org_map, trails_to_visit):
        self.org_map = org_map
        self.trails_to_visit = trails_to_visit
        # self.curr_pos = trails_to_visit[0]
        
        
    def scanDirections(self):
        next_height = self.height + 1
        
        if self.curr_pos in self.dirs_to_explore:
            return
        
        target_digit, target_pos = self.getDirectionDigit(Dir.UP)
        # print(target_digit)
        if target_digit == next_height:
            self.dirs_to_explore[self.curr_pos].append(Dir.UP)

        target_digit, target_pos = self.getDirectionDigit(Dir.DOWN)
        # print(target_digit)
        if target_digit == next_height:
            self.dirs_to_explore[self.curr_pos].append(Dir.DOWN)

        target_digit, target_pos = self.getDirectionDigit(Dir.LEFT)
        # print(target_digit)
        if target_digit == next_height:
            self.dirs_to_explore[self.curr_pos].append(Dir.LEFT)

        target_digit, target_pos = self.getDirectionDigit(Dir.RIGHT)
        # print(target_digit)
        if target_digit == next_height:
            self.dirs_to_explore[self.curr_pos].append(Dir.RIGHT)
        
        # print(self.dirs_to_explore)
        
        
    def walkPaths(self):
        for trail in self.trails_to_visit:
            self.dirs_to_explore = collections.defaultdict(list)
            self.curr_pos = trail
            self.height = 0
            self.discovered_nines = set()
            while True:
                sum_of_dirs_left_to_explore = 0
                prev_pos = self.curr_pos
                while True:
                    self.scanDirections()
                    print("dirs_to_explore", self.dirs_to_explore[self.curr_pos])
                    
                    if self.getDigit(self.curr_pos) == 9:
                        # if not self.curr_pos in self.discovered_nines:
                        #     self.discovered_nines.add(self.curr_pos)
                        self.sum_of_trail_points += 1
                        break
                    elif len(self.dirs_to_explore[self.curr_pos]) == 0:
                        break
                    
                    next_dir = self.dirs_to_explore[self.curr_pos][0]
                    # del self.dirs_to_explore[self.curr_pos][0]
                    self.moveDir(next_dir)
                    # print("curr_pos", self.curr_pos)
            
                new_pos = None
                all_paths_explored = True
                for key, value in self.dirs_to_explore.items():
                    # if len(value) > 0:
                        # new_pos = key
                        # self.curr_pos = key
                        # self.height = self.getDigit(self.curr_pos)
                    # sum_of_dirs_left_to_explore += len(value)
                    
                    if len(value) > 1:
                        new_pos = key
                        self.curr_pos = key
                        self.height = self.getDigit(self.curr_pos)
                        all_paths_explored = False
                # print("sum_of_dirs_left_to_explore", sum_of_dirs_left_to_explore)
                # print(self.dirs_to_explore)
                
                # if sum_of_dirs_left_to_explore == 0:
                if all_paths_explored :
                    break
                print("NEW POS", new_pos)
                del self.dirs_to_explore[new_pos][0]
                
                
            
    def moveDir(self, direction):
        print("Moving from", self.curr_pos)
        match direction:
            case Dir.UP:
                self.curr_pos = (self.curr_pos[0] - 1, self.curr_pos[1])
            case Dir.DOWN:
                self.curr_pos = (self.curr_pos[0] + 1, self.curr_pos[1])
            case Dir.LEFT:
                self.curr_pos = (self.curr_pos[0], self.curr_pos[1] - 1)
            case Dir.RIGHT:
                self.curr_pos = (self.curr_pos[0], self.curr_pos[1] + 1)
        self.height += 1
        print("Moved", direction, "To", self.curr_pos)
        

    def getDigit(self, pos_tuple):
        digit = self.org_map[pos_tuple[0]][pos_tuple[1]]
        if digit == ".":
            digit = -1
        return int(digit)
        
    def getDirectionDigit(self, direction):
        match direction:
            case Dir.UP:
                if self.curr_pos[0] != 0:
                    new_pos = (self.curr_pos[0] - 1, self.curr_pos[1])
                    return int(self.getDigit(new_pos)), new_pos
            case Dir.DOWN:
                if self.curr_pos[0] != len(self.org_map) - 1:
                    new_pos = (self.curr_pos[0] + 1, self.curr_pos[1])
                    return int(self.getDigit(new_pos)), new_pos
            case Dir.LEFT:
                if self.curr_pos[1] != 0:
                    new_pos = (self.curr_pos[0], self.curr_pos[1] - 1)
                    return int(self.getDigit(new_pos)), new_pos
            case Dir.RIGHT:
                if self.curr_pos[1] != len(self.org_map) - 1:
                    new_pos = (self.curr_pos[0], self.curr_pos[1] + 1)
                    return int(self.getDigit(new_pos)), new_pos
        return False, False
        

list1 = []
list2 = []
with open("ex_data.txt") as file:
    for i, row in enumerate(file):
        row_list = []
        for j, col in enumerate(row.strip()):
            row_list.append(col)
            if str(col) == "0":
                list2.append((i, j))
        list1.append(row_list)
# print(list2)

tail_walker_1 = Trailwalker(list1, list2)
tail_walker_1.walkPaths()
print(tail_walker_1.sum_of_trail_points)
# print(list1)