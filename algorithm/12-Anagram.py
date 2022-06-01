# 单词中的字母可以一一对应
# tea => eat listen => slient


# my test


from collections import Counter, defaultdict

def isAnagram(s1, s2):
    lst1 = sorted(list(s1))
    lst2 = sorted(list(s2))
    # if lst1 == lst2:
    #     return True
    # else:
    #     return False
    return lst1 == lst2

print(isAnagram('tea', 'eat'))


# First method
def isAnagram(s1, s2):
    map1 = {}
    map2 = {}
    for i in s1:
        if i in map1:
            map1[i] += 1

        else:
            map1[i] = 1
    for i in s2:
        if i in map2:
            map2[i] += 1

        else:
            map2[i] = 1
    return map1 == map2

print(isAnagram('listen', 'silented'))


# Second method
def isAnagram(s1, s2):
    d1 = Counter(s1,)
    d2 = Counter(s2)
    return d1 == d2
print(isAnagram('listen', 'silented'))

# Third method
def isAnagram(s1, s2):
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for i in s1:
        d1[i] += 1
    for i in s2:
        d2[i] += 1
    return d1 == d2
print(isAnagram('listen', 'silent'))