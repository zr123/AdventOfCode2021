def process_input(my_input):
    template = my_input[0].rstrip()
    rules = {}
    for line in my_input[2:]:
        polymer_in, insertion = line.rstrip().split(" -> ")
        rules[polymer_in] = insertion
    return template, rules


def init_polymer_summary(template, rules):
    polymer_summary = rules.copy()
    for k in polymer_summary.keys():
        polymer_summary[k] = 0

    for i in range(len(template)-1):
        polymer_summary[template[i:i+2]] += 1

    return polymer_summary


def polymer_insertion_step(polymer_summary, rules):
    new_polymer_summary = rules.copy()
    for k in new_polymer_summary.keys():
        new_polymer_summary[k] = 0

    for k, v in polymer_summary.items():
        new_polymer_summary[k[0] + rules[k]] += v
        new_polymer_summary[rules[k] + k[1]] += v

    return new_polymer_summary


def count_atoms(polymer_summary, initial_atom):
    atom_counts = {}
    for k, v in polymer_summary.items():
        letter = k[0]
        if not atom_counts.get(letter):
            atom_counts[letter] = 0
        atom_counts[letter] += v

    atom_counts[initial_atom] += 1
    return atom_counts


def polymorph_polymer(polymer_summary, rules, steps):
    for i in range(steps):
        polymer_summary = polymer_insertion_step(polymer_summary, rules)
    return polymer_summary


def part1(my_input):
    template, rules = process_input(my_input)
    polymer_summary = init_polymer_summary(template, rules)
    polymer_summary = polymorph_polymer(polymer_summary, rules, 10)
    atom_counts = count_atoms(polymer_summary, template[-1])
    sorted_value_counts = sorted(atom_counts.values())
    return sorted_value_counts[-1] - sorted_value_counts[0]


def part2(my_input):
    template, rules = process_input(my_input)
    polymer_summary = init_polymer_summary(template, rules)
    polymer_summary = polymorph_polymer(polymer_summary, rules, 40)
    atom_counts = count_atoms(polymer_summary, template[-1])
    sorted_value_counts = sorted(atom_counts.values())
    return sorted_value_counts[-1] - sorted_value_counts[0]
