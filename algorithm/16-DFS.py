# DFS: Depth First Search, 从最左侧由根向下遍历，对象有未被遍历的叶时继续往下遍历，无未被遍历叶时向上返回，返回到根时退出。
nums = [2, 0, 3, 1, 3, 4]
pst = 3
def dfs(nums, p, t=0, nb=set()):
    step = nums[p]
    if p - step < 0 and p + step > len(nums):
        return False
    if nums[p - step] == t or nums[p + step] == t:
        return p - step or p + step
    else:
        return dfs(nums, p - step , t) or f(nums, p + step , t)

print(dfs(nums, pst))

