# 最大公约数GCD(Greatest Common Divisor)和最小公倍数LCM

# GCD(25， 35) = 5, LCM(25, 35) = 25 * 35 / GCD(25, 35)
# 如何求最大公约数，欧几里得算法又称辗转相除法，是指用于计算两个非负整数a，b的最大公约数。
# 应用领域有数学和计算机两个方面。计算公式gcd(a,b) = gcd(b,a mod b)。

import gc


def gcd(a, b):
    # 最大公约数可以是1，这两行注释掉
    # if a % b == 1:
    #     return -1
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
    
print(gcd(30, 36))

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a
print(gcd(30, 36))


# 最小公倍数LCM(least common multiple),等于两数乘积除以最小公倍数
# First method: GCD算法
def lcm(a, b):
    return a * b // gcd(a, b)
print(lcm(6, 15))

# Second method: 乘法穷举
def lcm(a, b):
    if a < b:
        a, b = b, a
    for i in range(1, b+1):
        if a * i % b == 0:
            return a*i
print(lcm(14, 15)) 