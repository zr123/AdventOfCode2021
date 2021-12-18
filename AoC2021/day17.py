import re


def process_input(my_input):
    p = re.compile("^target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)$")
    m = p.match(my_input[0])
    min_x, max_x, min_y, max_y = m.groups()
    return int(min_x), int(max_x), int(min_y), int(max_y)


def calc_valid_y_velocities(min_y, max_y):
    valid_y_velocities = set()
    for starting_y_velocity in range(-500, 500):
        y_speed = starting_y_velocity
        y_position = 0
        # simulate
        while True:
            y_position += y_speed
            y_speed -= 1
            if min_y <= y_position <= max_y:
                valid_y_velocities.add(starting_y_velocity)
            if y_position < min_y:
                break

    return valid_y_velocities


def part1(my_input):
    _, _, min_y, max_y = process_input(my_input)
    valid_y_velocities = calc_valid_y_velocities(min_y, max_y)
    return sum(range(max(valid_y_velocities)+1))


def calc_valid_x_velocities(min_x, max_x):
    valid_x_velocities = set()
    for starting_x_velocity in range(500):
        x_speed = starting_x_velocity
        x_position = 0
        # simulate
        while True:
            x_position += x_speed
            if x_speed > 0:
                x_speed -= 1
            if min_x <= x_position <= max_x:
                valid_x_velocities.add(starting_x_velocity)
            if x_position > max_x or x_speed == 0:
                break
    return valid_x_velocities


def validate_velocities(x, y, min_x, max_x, min_y, max_y):
    # simulate
    x_pos, y_pos = 0, 0
    x_speed, y_speed = x, y
    while True:
        x_pos += x_speed
        y_pos += y_speed
        if x_speed > 0:
            x_speed -= 1
        y_speed -= 1
        if (min_y <= y_pos <= max_y) and (min_x <= x_pos <= max_x):
            return True
        if x_pos > max_x or y_pos < min_y:
            return False


def part2(my_input):
    min_x, max_x, min_y, max_y = process_input(my_input)
    valid_x_velocities = calc_valid_x_velocities(min_x, max_x)
    valid_y_velocities = calc_valid_y_velocities(min_y, max_y)
    # validate all possible combinations
    count = 0
    for x in valid_x_velocities:
        for y in valid_y_velocities:
            if validate_velocities(x, y, min_x, max_x, min_y, max_y):
                count += 1
            print(x, y)

    return count
