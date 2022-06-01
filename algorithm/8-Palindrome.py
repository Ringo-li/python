# Palindrome : a word like racecar, we can celled it palindrome
s = 'bbacracecarabcdadad'

# The first method
# 如果一个字符串反过来等于他本身，这个字符串就是回文字符串
# def isPalindrome(s):
#     return rev(s) == s
        
# def rev(s):
#     # tmp = ''
#     # for i in s:
#     #     tmp = i + tmp
#     # return tmp
#     return s[::-1]

# The second method
# 一个字符串左边和右边的值总相等，这个字符串就是回文字符串
# def isPalindrome(s):
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         if s[left] == s[right]:
#             left += 1
#             right -= 1
#         else:
#             return False
#     return True

# print(isPalindrome('racecara'))

# The third method
# 使用堆栈来确定回文字符
def isPalindrome(s):
    arr = list(s)
    for i in s[:len(s)//2+1]:
        if i != arr.pop():
            return False
        print(i)
    return True
    
print(isPalindrome('racecar'))
