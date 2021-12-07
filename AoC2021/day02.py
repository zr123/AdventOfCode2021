class Submarine:
    def __init__(self, commands=None):
        self.x = 0
        self.depth = 0
        if commands is not None:
            self.take_commands(commands)

    def take_command(self, command):
        command, value = command.split()
        if command == "forward":
            self.x += int(value)
        elif command == "down":
            self.depth += int(value)
        elif command == "up":
            self.depth -= int(value)
            if self.depth < 0:
                self.depth = 0
        else:
            raise Exception("Unhandled command!")

    def take_commands(self, commands):
        for command in commands:
            self.take_command(command)

    def get_positional_value(self):
        return self.x * self.depth


def part1(my_input):
    sub = Submarine(my_input)
    return sub.get_positional_value()


class AimedSubmarine(Submarine):
    def __init__(self, commands=None):
        self.aim = 0
        super().__init__(commands)

    def take_command(self, command):
        command, value = command.split()
        if command == "forward":
            self.x += int(value)
            self.depth += int(value) * self.aim
            if self.depth < 0:
                self.depth = 0
        elif command == "down":
            self.aim += int(value)
        elif command == "up":
            self.aim -= int(value)
        else:
            raise Exception("Unhandled command!")


def part2(my_input):
    sub = AimedSubmarine(my_input)
    return sub.get_positional_value()
