def testA(a, b):
    print(a + b)

def testB(a, b):
    print(a + b)

# all列表添加功能
__all__ = ['testA']
if __name__ == "__main__":
    testA(1, 2)
    testB(2, 2)