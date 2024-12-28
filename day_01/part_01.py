with open('input.txt') as f:
    lines = f.readlines()
    
    left_num = []
    right_num = []

    for line in lines:
        nums = line.split('   ')
        left_num.append(nums[0])
        right_num.append(nums[1].split('\n')[0])

    left_num.sort()
    right_num.sort()

    dist_sum = 0
    i = 0

    while i < len(left_num):
        dist_sum = dist_sum + abs((int(left_num[i]) - int(right_num[i])))
        i = i + 1

    print(dist_sum) 