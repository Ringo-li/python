# 需求：3以内数字累加和
# 6 = 3+2以内数字累加和
# 2以内数字累加和=2+
# 1以内数字累加和=1

def sum(num):
    # 2.出口
    if num == 1:
        return 1
    # 1.当前数字+当前数字-1累加和
    return num + sum(num - 1)

result = sum(3)
print(result)