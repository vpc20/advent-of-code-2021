from aoc_tools import read_input_to_nums

if __name__ == '__main__':
    # f = open('aoc_2_testdata1.txt')
    f = open('aoc_2_data1.txt')
    commands = [line.strip().split() for line in f]
    f.close()

    hpos, depth, aim = 0, 0, 0

    for comm, val in commands:
        val = int(val)
        if comm == 'forward':
            hpos += val
            depth += aim * val
        elif comm == 'down':
            aim += val
        else:
            aim -= val

    prod = hpos * depth
    print(prod)
