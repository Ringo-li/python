# BFS: Breadth First Search, 依次遍历树的每一行
# DFS: Depth First Search, 从最左侧由根向下遍历，对象有未被遍历的叶时继续往下遍历，无未被遍历叶时向上返回，返回到根时退出。

# 列题：给一个数字列表，再给定一个起始位置，该位置的数值是能够在列表中左右移动的步数，求最终能不能找到数字0
nums = [2, 0, 3, 1, 3, 4]
pst = 5

# 利用队列queue 先进先出的性质
def bfs(nums, p):
    queue = [p]
    while queue:
        step = queue.pop(0)
        if step < 0 or step > len(nums):
            return False
        if nums[step] == 0:
            return True
        newp1 = step - nums[step]
        newp2 = step + nums[step]
        if newp1 >= 0:
            queue.append(newp1)
        if newp2 < len(nums):
            queue.append(newp2)
    return False
print(bfs(nums, pst))

        
    



# def f(nums, p, t=0):
#     step = nums[p]
#     if p - step < 0 and p + step > len(nums):
#         return False
#     if nums[p - step] == t or nums[p + step] == t:
#         return p - step or p + step
#     else:
#         return f(nums, p - step , t) or f(nums, p + step , t)

# print(f(nums, pst))