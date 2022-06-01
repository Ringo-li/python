# Average, sum of the numbers divided by how many numbers are in the list.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,20, 2000]
def average(nums):
    s = 0
    for i in nums:
        s += i
    return '{:.1f}'.format(s / len(nums))
# In python, these can replace by fuction: sum
    # return sum(nums)/len(nums)

print(average(nums))

# Median, the median is the value separating the higher half from the lower half of a data sample.
# 中位数：一个从小到大排序的列表，位置在中间的数，奇数列表有一个，偶数列表为中间两个数的平均值。
def median(nums):
    nums.sort()
    if len(nums) % 2:
        return nums[len(nums)//2]
    else:
        return (nums[len(nums)//2-1] + nums[len(nums)//2])/2        
print(median(nums))

