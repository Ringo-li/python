class Furniture():
    def __init__(self, name, area):
        # 家具名称
        self.name = name
        # 家具占地面积
        self.area = area

class Home():
    def __init__(self, address, area):
        # 地址
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房子在{self.address}，面积{self.area}，剩余面积{self.free_area}，家里列表{self.furniture}'

    def add_furniture(self, item):
        # 判断，当剩余面积大于家具面积时，将家具添加到家具列表,并刷新房屋可用面积
        if item.area < self.free_area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('furnitrue is too big to move in house')

# 双人床
bed = Furniture('床', 2*3)
bar = Furniture('茶几', 2*1)
squre = Furniture('空闲', 5*6)
table = Furniture('餐桌', 2*1.5)

# 房子
fangjian1 = Home('西安', 40)
print(fangjian1)

# 搬家具
fangjian1.add_furniture(bed)
print(fangjian1)
fangjian1.add_furniture(bar)
print(fangjian1)
fangjian1.add_furniture(squre)
print(fangjian1)
fangjian1.add_furniture(table)
print(fangjian1)