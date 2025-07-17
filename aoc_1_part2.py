from aoc_tools import read_input_to_nums

if __name__ == '__main__':
    # f = open('aoc_1_testdata1.txt')
    f = open('aoc_1_data1.txt')
    nums = [int(line.strip()) for line in f]
    f.close()

    ctr = 0
    for i in range(len(nums) - 3):
        if nums[i + 1] + nums[i + 2] + nums[i + 3] > nums[i] + nums[i + 1] + nums[i + 2]:
            ctr += 1
    print(ctr)

    # one-liner
    print(len([True for i in range(len(nums) - 3) if
               nums[i + 1] + nums[i + 2] + nums[i + 3] > nums[i] + nums[i + 1] + nums[i + 2]]))
