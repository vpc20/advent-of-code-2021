from aoc_tools import read_input_to_nums

if __name__ == '__main__':
    # f = open('aoc_1_testdata1.txt')
    f = open('aoc_1_data1.txt')
    nums = [int(line.strip()) for line in f]
    f.close()

    prev = nums[0]
    ctr = 0

    for num in nums[1:]:
        if num > prev:
            ctr +=1
        prev = num

    print(ctr)

    # one-liner
    print(len([True for i in range(1, len(nums)) if nums[i] > nums[i-1]]))



