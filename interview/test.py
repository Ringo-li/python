candidates = [2,3,6,7]
target = 7

path = []
result = []
# 回溯，在for循环中嵌套递归
def backtracking(nums, target, startindex):
    # 1.确定参数，数组，startindex，
    # 2.确定终止条件和收获返回值
    if sum(path) > target:
        return
    if sum(path) == target:
        result.append(path.copy())
        return

    # 3.确定单层逻辑
    for i in range(startindex, len(nums)):
        path.append(nums[i])
        backtracking(nums, target, i)
        path.pop()

backtracking(candidates, 7, 0)
print(result)
        
