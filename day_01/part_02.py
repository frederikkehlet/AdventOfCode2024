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

    score = 0
    
    for num in left_num:
        matches = [n for n in right_num if n == num]
        
        if len(matches) != 0:
            score = score + (int(num) * len(matches))

    print(score)

