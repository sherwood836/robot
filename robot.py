cardinal_list = ['N', 'E', 'S', 'W']
cardinal_pos_map = {'N':0, 'E':1, 'S':2, 'W':3}

def turn_right(x, y, direction):
    return x, y, cardinal_list[(cardinal_pos_map[direction] + 1) % 4]

def turn_left(x, y, direction):
    return x, y, cardinal_list[(cardinal_pos_map[direction] - 1) % 4]

def move_1(x, y, direction):
    if 'N' == direction:
        y = y + 1
    elif 'S' == direction:
        y = y - 1
    elif 'E' == direction:
        x = x + 1
    elif 'W' == direction:
        x = x - 1

    return x, y, direction

def make_move(x, y, direction, move):
    if 'M' == move:
        x, y, direction = move_1(x, y, direction)
    elif 'L' == move:
        x, y, direction = turn_left(x, y, direction)
    elif 'R' == move:
        x, y, direction = turn_right(x, y, direction)
    else:
        raise Exception(f"Invalid move:[{move}]")

    return x, y, direction

def take_trip(x, y, direction, move_list):
        for move in move_list:
           x, y, direction = make_move(int(x), int(y), direction, move) 

        return x, y, direction

def error_check_start(start_position):
    if not start_position:
        return None

    position_list = start_position.split(' ')

    if len(position_list) == 3:
        x, y, direction = position_list
    else:
        raise Exception(f"Invalid start position:[{start_position}]")

    x = error_check_coordinate(x, "Invalid start position x coordinate") 
    y = error_check_coordinate(y, "Invalid start position y coordinate") 

    if direction not in cardinal_list:
        raise Exception(f"Invalid start position direction:[{direction}]")

    return x, y, direction

def error_check_coordinate(coordinate, error_message):
    try:
        coordinate = int(coordinate)
    except:
        raise Exception(f"{error_message}:[{coordinate}]")

    if coordinate < 0:
        raise Exception(f"{error_message}:[{coordinate}]")
    
    return coordinate

def error_check_max(max_position):
    max_position_list = max_position.split(' ')

    if len(max_position_list) == 2:    
        x, y = max_position_list
    else:
        raise Exception(f"Invalid max coordinates given:[{max_position}]")

    x = error_check_coordinate(x, "Invalid max x coordinate") 
    y = error_check_coordinate(y, "Invalid max y coordinate") 

    return x, y

def program():
    output_print_list = []

    max_x, max_y = error_check_max(input())
    start_position = error_check_start(input())

    while start_position:
        x, y, direction = start_position
        move_list = input()
        x, y, direction = take_trip(x, y, direction, move_list)
        output_print_list.append(f"{x} {y} {direction}")
        start_position = error_check_start(input())

    return output_print_list


if __name__ == '__main__':
    output_print_list = program()

    for line in output_print_list:
        print(line)
