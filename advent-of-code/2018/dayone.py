import operator
import sys


def main(input_filename):
    changes = load_changes(input_filename)
    print(compute_resulting_frequency(changes))


def load_changes(input_filename):
    changes = []
    
    with open(input_filename) as f:
        for line in f:
            changes.append(int(line.strip()))
            
    return changes


def compute_resulting_frequency(changes):
    return reduce(opearator.add, changes, 0)


if __name__ == '__main__':
    main(sys.argv[1])
