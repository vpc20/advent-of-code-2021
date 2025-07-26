from collections import Counter

from aoc_tools import read_input_to_grid

if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_3_testdata1.txt')
    grid = read_input_to_grid('aoc_3_data1.txt')

    grid = list(zip(*grid))  # transpose grid

    for e in grid:
        print(e)

    gamma_rate_binary = ''
    epsilon_rate_binary = ''

    for bits in grid:
        ctr_bits = Counter(bits)
        print(ctr_bits)
        if ctr_bits['1'] > ctr_bits['0']:
            gamma_rate_binary += '1'
            epsilon_rate_binary += '0'
        else:
            gamma_rate_binary += '0'
            epsilon_rate_binary += '1'

    power_consumption = int(gamma_rate_binary, 2) * int(epsilon_rate_binary, 2)
    print(power_consumption)
