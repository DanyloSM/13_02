nums = [1, 2, 3, 4, 5, 6]
mid_nums = (len(nums) + 1) // 2  #=> [[1, 2, 3], [4, 5, 6]]
result = [nums[:mid_nums], nums[mid_nums:]]
print(result)
#nums = [1, 2, 3] #=> [[1, 2], [3]]
#mid_nums = (len(nums) + 1) // 2
#result = [nums[:mid_nums], nums[mid_nums:]]
#print(result)
#nums = [1, 2, 3, 4, 5] #=> [[1, 2, 3], [4, 5]]
#mid_nums = (len(nums) + 1) // 2
#result = [nums[:mid_nums], nums[mid_nums:]]
#print(result)
#nums = [1] #=> [[1], []]
#mid_nums = (len(nums) + 1) // 2
#result = [nums[:mid_nums], nums[mid_nums:]]
#print(result)
#nums = [] #=> [[], []]
#mid_nums = (len(nums) + 1) // 2
#result = [nums[:mid_nums], nums[mid_nums:]]
#print(result)









