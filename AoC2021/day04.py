import numpy as np


def process_input(raw_input):
    instructions = np.array(raw_input[0].rstrip().split(","), dtype=float)
    boards = []
    for i in range(2, len(raw_input), 6):
        board = np.array([s.lstrip().rstrip().replace("  ", " ").split(" ") for s in raw_input[i:i+5]], dtype=float)
        boards.append(board)
    return instructions, np.array(boards)


def is_finished(board):
    for row in board:
        if np.sum(np.isnan(row)) == 5:
            return True
    # cols
    for i in range(5):
        if np.sum(np.isnan(board[:, i])) == 5:
            return True
    return False


def calc_board_sum(board):
    return np.sum(board[~np.isnan(board)])


def part1(my_input):
    instructions, boards = process_input(my_input)
    for i in instructions:
        boards[boards == i] = np.NAN
        for board in boards:
            if is_finished(board):
                board_sum = calc_board_sum(board)
                return board_sum * i

    raise Exception("This should never happen.")


def part2(my_input):
    instructions, boards = process_input(my_input)
    for i in instructions:
        boards[boards == i] = np.NAN
        remove = []
        for b in range(len(boards)):
            if is_finished(boards[b]):
                remove.append(b)

        if boards.shape[0] > 1:
            boards = np.delete(boards, remove, 0)
        else:
            board_sum = calc_board_sum(boards[0])
            return board_sum * i

    raise Exception("This should never happen.")
