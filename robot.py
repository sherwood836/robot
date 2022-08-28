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
    else:
        raise Exception(f"Invalid direction:[{direction}]")

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

def take_trip(start_position, move_list):
        position_list = start_position.split(' ')

        if len(position_list) == 3:
            x, y, direction = position_list
        else:
            raise Exception(f"Invalid start position:[{start_position}]")

        for move in move_list:
           x, y, direction = make_move(int(x), int(y), direction, move) 

        return x, y, direction

def program():
    output_print_list = []

    max_position = input()
    max_position_list = max_position.split(' ')

    if len(max_position_list) == 2:    
        max_x, max_y = max_position_list
    else:
        raise Exception(f"Invalid max coordinates given:[{max_position}]")

    start_position = input()

    while start_position:
        move_list = input()
        x, y, direction = take_trip(start_position, move_list)
        output_print_list.append(f"{x} {y} {direction}")
        start_position = input()

    return output_print_list

if __name__ == '__main__':
    output_print_list = program()

    for line in output_print_list:
        print(line)
