# 123 => 1 + 2 + 3 = 6

# my test
def f(n):
    return sum([int(i) for i in list(str(n))])
print(f(3))

# First method
def f(n):
    ans = 0
    while n >= 1:
        ans += n%10
        n //= 10
    return ans

print(f(123))

# Second method
def f(n):
    if n == 0:
        return 0
    return n%10 + f(n//10)
print(f(1234))