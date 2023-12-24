def is_right_open(path, map, last_row, last_col):
    row = path[0][-1][0]
    col = path[0][-1][1] + 1
    if (col == last_col or (map[row][col] == 1 and path[1]) or [row,col] in path[0]):
        return False
    if (map[row][col] == 1):
        path[1] = True
    return True
    
def is_left_open(path, map, last_row, last_col):
    row = path[0][-1][0]
    col = path[0][-1][1] -1
    if (col < 0 or (map[row][col] == 1 and path[1]) or [row,col] in path[0]):
        return False
    if (map[row][col] == 1):
        path[1] = True
    return True
    
def is_up_open(path, map, last_row, last_col):
    row = path[0][-1][0] - 1
    col = path[0][-1][1]
    if (row < 0 or (map[row][col] == 1 and path[1]) or [row,col] in path[0]):
        return False
    if (map[row][col] == 1):
        path[1] = True
    return True
    
def is_down_open(path, map, last_row, last_col):
    row = path[0][-1][0] + 1
    col = path[0][-1][1]
    if (row == last_row or (map[row][col] == 1 and path[1]) or [row,col] in path[0]):
        return False
    if (map[row][col] == 1):
        path[1] = True
    return True

def right_move(pos):
    return [pos[-1][0], pos[-1][1] + 1]

def left_move(pos):
    return [pos[-1][0], pos[-1][1] - 1]

def down_move(pos):
    return [pos[-1][0] + 1, pos[-1][1]]

def up_move(pos):
    return [pos[-1][0] - 1, pos[-1][1]]

def plan(path, wall_removed):
    return [path[:], wall_removed]

def solution(map):
    start = [0,0]
    last_row = len(map)
    last_col = len(map[0])
    end = [last_row - 1, last_col - 1]
    unfinished_paths = [[start[:]]]
    finished_paths = []
    shortest_path = last_row * last_col
    count = 1
    
    start_path = plan([[0, 0]], False)
    
    current_paths = [start_path]
    next_paths = []
    
    while True:
        count = count + 1
        
        for path in current_paths:
            if(is_right_open(path, map, last_row, last_col)):
                new_path = plan(path[0], path[1])
                new_path[0].append(right_move(new_path[0]))
                if(end == new_path[0][-1]):
                    return count
                next_paths.append(new_path)
            if(is_down_open(path, map, last_row, last_col)):
                new_path = plan(path[0], path[1])
                new_path[0].append(down_move(new_path[0]))
                if(end == new_path[0][-1]):
                    return count
                next_paths.append(new_path)
            if(is_up_open(path, map, last_row, last_col)):
                new_path = plan(path[0], path[1])
                new_path[0].append(up_move(new_path[0]))
                if(end == new_path[0][-1]):
                    return count
                next_paths.append(new_path)
            if(is_left_open(path, map, last_row, last_col)):
                new_path = plan(path[0], path[1])
                new_path[0].append(left_move(new_path[0]))
                if(end == new_path[0][-1]):
                    return count
                next_paths.append(new_path)
        if end in next_paths:
            return count
        current_paths = next_paths
        next_paths = []
