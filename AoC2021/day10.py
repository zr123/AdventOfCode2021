

def check_chunk(chunk):
    chunk = chunk.rstrip()
    expected_closing_chars = []
    for char in chunk:
        if char == "{":
            expected_closing_chars.append("}")
            continue
        if char == "<":
            expected_closing_chars.append(">")
            continue
        if char == "[":
            expected_closing_chars.append("]")
            continue
        if char == "(":
            expected_closing_chars.append(")")
            continue

        expected_char = expected_closing_chars.pop()
        if expected_char != char:
            if char == ")":
                return 3
            if char == "]":
                return 57
            if char == "}":
                return 1197
            if char == ">":
                return 25137
    return 0


def part1(my_input):
    sum = 0
    for chunk in my_input:
        sum += check_chunk(chunk)
    return sum


def get_chunk_completion_score(chunk):
    chunk = chunk.rstrip()
    expected_closing_chars = []
    for char in chunk:
        if char == "{":
            expected_closing_chars.append("}")
            continue
        if char == "<":
            expected_closing_chars.append(">")
            continue
        if char == "[":
            expected_closing_chars.append("]")
            continue
        if char == "(":
            expected_closing_chars.append(")")
            continue

        expected_char = expected_closing_chars.pop()
        # corrupted
        if expected_char != char:
            return 0

    score = 0
    for char in reversed(expected_closing_chars):
        score *= 5
        if char == ")":
            score += 1
        if char == "]":
            score += 2
        if char == "}":
            score += 3
        if char == ">":
            score += 4
    return score


def part2(my_input):
    scores = []
    for chunk in my_input:
        score = get_chunk_completion_score(chunk)
        if score != 0:
            scores.append(score)

    scores = sorted(scores)
    return scores[len(scores)//2]
