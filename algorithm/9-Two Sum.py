# 给定一个列表，从列表中取出两个数，其和等于目

nums = [5, 3, 4, 6, 7, 1]
target = 14

# First method
# 暴力遍历
# def twoSum(nums, t):
#     tmp = []
#     for i in range(len(nums)):
#         for j in range(i+1):
#             if nums[i] + nums[j] == t:
#                 tmp.append([nums[i],nums[j]])
#     return tmp

# print(twoSum(nums, target))

# Second method
# 使用字典,notebook
# def twoSum(nums, t):
#     nb = []
#     for i in nums:
#         tmp = t - i 
#         if tmp in nb:
#             return True
#         nb.append(i)
#     return False
# print(twoSum(nums, target))


# Third method
# 先排序，两数和小于目标值左值往右移，大于目标值右值往左移
nums.sort()
def twoSum(num, t):
    left = 0
    right = len(nums) - 1
    while left < right:
        count = num[left] + num[right]
        if count == t:
            return True
        elif count < t:
            left += 1
        else:
            right -= 1
    return False
print(twoSum(nums, target))


