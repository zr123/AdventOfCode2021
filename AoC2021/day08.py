import numpy as np


def process_input(my_input):
    signals, output_signals = [], []
    for line in my_input:
        pattern, output_signal = line.rstrip().split(" | ")
        signals.append(pattern.split(" "))
        output_signals.append(output_signal.split(" "))
    return np.array(signals), np.array(output_signals)


def part1(my_input):
    _, output_signals = process_input(my_input)
    myfunc = np.vectorize(lambda p: 1 if len(p) in [2, 4, 3, 7] else 0)
    return np.sum(myfunc(output_signals))


# it's sufficient to know the signal-patterns of number 1 and number 4 to deduce the rest
def pattern_to_number(input_pattern, one_pattern, four_pattern):
    pattern_length = len(input_pattern)
    if pattern_length == 2:
        return 1
    if pattern_length == 3:
        return 7
    if pattern_length == 4:
        return 4
    if pattern_length == 7:
        return 8

    set_input = set(input_pattern)
    set_one = set(one_pattern)
    set_four = set(four_pattern)
    # numbers containing five signals [2, 3, 5]
    if pattern_length == 5:
        if len(set_input & set_one) == 2:
            return 3
        if len(set_input & set_four) == 3:
            return 5
        return 2
    # numbers containing five signals [0, 6, 9]
    if pattern_length == 6:
        if len(set_input & set_four) == 4:
            return 9
        if len(set_input & set_one) == 2:
            return 0
        return 6
    raise Exception("Impossible signal pattern received.")


def output_signals_to_number(output_signal, one_signal, four_signal):
    result = 0
    for pattern in output_signal:
        result *= 10
        result += pattern_to_number(pattern, one_signal, four_signal)
    return result


def part2(my_input):
    signals, output_signals = process_input(my_input)
    sum_total = 0
    for signal, output_signal in zip(signals, output_signals):
        for s in signal:
            if len(s) == 2:
                one_signal = s
            if len(s) == 4:
                four_signal = s
        sum_total += output_signals_to_number(output_signal, one_signal, four_signal)
    return sum_total
