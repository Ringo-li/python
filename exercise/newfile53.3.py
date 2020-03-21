
class MusicPlayer(object):
 
    # 定义类属性记录创建对象的引用初始值设为None
    instance = None
 
    init_flag = False
 
    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为None
        if cls.instance is None:
            # 2.如果对象还没有被创建，就调用父类的方法为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3.把类属性中保存的引用返回给Python的解释器
        return cls.instance
 
    def __init__(self):
        #if MusicPlayer.init_flag:
        if self.init_flag:
            return
 
        print("初始化播放器")
        #MusicPlayer.init_flag = True
        self.init_flag = True
 
 
player1 = MusicPlayer()
print(player1)
 
player2 = MusicPlayer()
print(player2)