operations = input().split('-')
min_nums = []
for op in operations:
    nums = list(map(int, op.split('+')))
    sum_of_nums = 0
    for num in nums:
        sum_of_nums += num
    min_nums.append(sum_of_nums)

result = min_nums[0]
for i in range(1, len(min_nums)):
    result -= min_nums[i]

print(result)