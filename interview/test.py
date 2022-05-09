nums = [2, 5, 7, 3, 2, 6, 2, 4, 1]
path = []
resault = []
def backtracking(nums, startindex):
    if len(path) == 3:
        if path[0]**3 + path[1]**3 + path[2] == path[0]*100 + path[1]*10 + path[2]:
            resault.append(path.copy())
        return
    if len(path) > 3:
        return
    for i in range(startindex, len(nums)):
        path.append(nums[i])
        backtracking(nums, 0)
        path.pop()   
backtracking(nums, 0)
print(resault)