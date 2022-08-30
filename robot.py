cardinal_list = ['N', 'E', 'S', 'W']
cardinal_pos_map = {'N':0, 'E':1, 'S':2, 'W':3}

def turn_right(x: int, y: int, direction: str) -> tuple:
    return x, y, cardinal_list[(cardinal_pos_map[direction] + 1) % 4]

def turn_left(x: int, y: int, direction: str) -> tuple:
    return x, y, cardinal_list[(cardinal_pos_map[direction] - 1) % 4]

def move_1(x: int, y: int, direction: str, max_x: int, max_y: int) -> tuple:
    if 'N' == direction:
        y = (y + 1) if y != max_y else y
    elif 'S' == direction:
        y = (y - 1) if y != 0 else y
    elif 'E' == direction:
        x = (x + 1) if x != max_x else x
    elif 'W' == direction:
        x = (x - 1) if x != 0 else x

    return x, y, direction

def make_move(x: int, y: int, direction: str, move: str, max_x: int, max_y: int) -> tuple:
    if 'M' == move:
        x, y, direction = move_1(x, y, direction, max_x, max_y)
    elif 'L' == move:
        x, y, direction = turn_left(x, y, direction)
    elif 'R' == move:
        x, y, direction = turn_right(x, y, direction)
    else:
        raise Exception(f"Invalid move:[{move}]")

    return x, y, direction

def take_trip(x: int, y: int, direction: str, move_list: str, max_x: int, max_y: int) -> tuple:
        for move in move_list:
           x, y, direction = make_move(int(x), int(y), direction, move, max_x, max_y) 

        return x, y, direction

def error_check_start(start_position: str, max_x: int, max_y: int) -> tuple:
    if not start_position:
        return None

    position_list = start_position.split(' ')

    if len(position_list) == 3:
        x, y, direction = position_list
    else:
        raise Exception(f"Invalid start position:[{start_position}]")

    x = error_check_coordinate(x, max_x, "Invalid start position x coordinate") 
    y = error_check_coordinate(y, max_y, "Invalid start position y coordinate") 

    if direction not in cardinal_list:
        raise Exception(f"Invalid start position direction:[{direction}]")

    return x, y, direction

def error_check_coordinate(coordinate: str, max_coordinate: int, error_message: str) -> int:
    try:
        coordinate = int(coordinate)
    except:
        raise Exception(f"{error_message}:[{coordinate}]")

    if coordinate < 0:
        raise Exception(f"{error_message}:[{coordinate}]. Should be greater than 0.")
    
    if max_coordinate is not None and coordinate > max_coordinate:
        raise Exception(f"{error_message}:[{coordinate}]. Should be less than or equal to {max_coordinate}.")
    
    return coordinate

def error_check_max(max_position: str) -> tuple:
    max_position_list = max_position.split(' ')

    if len(max_position_list) == 2:    
        x, y = max_position_list
    else:
        raise Exception(f"Invalid max coordinates given:[{max_position}]")

    x = error_check_coordinate(x, None, "Invalid max x coordinate") 
    y = error_check_coordinate(y, None, "Invalid max y coordinate") 

    return x, y

def program() -> list:
    output_print_list = []

    max_x, max_y = error_check_max(input())
    start_position = error_check_start(input(), max_x, max_y)

    while start_position:
        x, y, direction = start_position
        move_list = input()
        x, y, direction = take_trip(x, y, direction, move_list, max_x, max_y)
        output_print_list.append(f"{x} {y} {direction}")
        start_position = error_check_start(input(), max_x, max_y
        )

    return output_print_list


if __name__ == '__main__':
    output_print_list = program()

    for line in output_print_list:
        print(line)
