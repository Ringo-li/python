# My test method
class Solution:
    def reverseWords(self, s: str) -> str:
        slst = s.split()
        result = []
        for i in slst:
            tmp = ''
            lsti = list(i)
            lsti.reverse()
            for j in lsti:
                tmp += j
            result.append(tmp)
        return ' '.join(result)

obj = Solution()
s = "Let's take LeetCode contest"
print(obj.reverseWords(s))

# First method 字符串反转[::-]
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(i[::-1] for i in s.split())

obj = Solution()
s = "Let's take LeetCode contest"
print(obj.reverseWords(s))