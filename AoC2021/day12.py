def remove_cave_from_paths(cave, remaining_paths):
    paths = []
    for p in remaining_paths:
        if cave not in p:
            paths.append(p)
    return paths


def traverse(current, cave_connections):
    if current == "end":
        return 1

    paths = 0
    for i, next_path in enumerate(cave_connections):
        cave1, cave2 = next_path.split("-")
        # is reachable
        if current == cave1 or current == cave2:
            if current == cave1:
                next_cave = cave2
            else:
                next_cave = cave1

            if current.isupper():
                paths += traverse(next_cave, cave_connections)
            else:
                paths += traverse(next_cave, remove_cave_from_paths(current, cave_connections))

    return paths


def part1(my_input):
    my_input = [i.rstrip() for i in my_input]
    return traverse("start", my_input)


def get_small_caves(cave_connections):
    small_caves_dict = {}
    for connection in cave_connections:
        cave1, cave2 = connection.split("-")
        if cave1.islower():
            small_caves_dict[cave1] = 0
        if cave2.islower():
            small_caves_dict[cave2] = 0

    return small_caves_dict


def remove_visited_small_caves(cave_connections, small_caves_dict):
    paths = cave_connections.copy()
    for k, v in small_caves_dict.items():
        if v >= 1:
            paths = remove_cave_from_paths(k, paths)

    return paths


def has_visited_twice(small_caves_dict):
    for v in small_caves_dict.values():
        if v >= 2:
            return True
    return False


def traverse2(current, cave_connections, small_caves_dict):
    if current == "end":
        return 1

    valid_connections = cave_connections.copy()
    if has_visited_twice(small_caves_dict):
        valid_connections = remove_visited_small_caves(cave_connections, small_caves_dict)
    paths = 0

    for i, next_path in enumerate(valid_connections):
        cave1, cave2 = next_path.split("-")
        # is reachable
        if current == cave1 or current == cave2:
            if current == cave1:
                next_cave = cave2
            else:
                next_cave = cave1
            if next_cave == "start":
                continue

            new_caves_dict = small_caves_dict.copy()
            if current.islower():
                new_caves_dict[current] += 1
            paths += traverse2(
                next_cave,
                valid_connections,
                new_caves_dict
            )

    return paths


# buggy and slow :(
def part2(my_input):
    my_input = [i.rstrip() for i in my_input]
    small_caves_dict = get_small_caves(my_input)
    return traverse2("start", my_input, small_caves_dict)
