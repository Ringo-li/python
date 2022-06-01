# A tree have root, leaves and trunk.
# Binary tree, a parent can have at most two children, we can cell it right and left.
# perfect binary tree the depth and node number: 2**d -1

# How to store a perfect binary tree into computer:
# a perfect binary tree's node like [0, 1, 2, 3, 4, 5, 6], how to use parent to get their children?
# left = parent * 2 + 1, right = parent * 2 + 2
# how to store a  perfect binary tree  into a queue
# 将根节点存入队列，pop出队列中第一个node，目前只有根节点，pop出的同时存入根节点的两个子节点，
# 再依次pop第一个节点（及根节点的left），在queue中存入根节点left的两个字节点，直到遇到没有子节点的node后退出。

# binary search tree it means that the left nodes always smaller than parent but right node always big than parent
#   

