from django.db import models

# Create your models here.
"""
1.ORM
    表 --> 类
    字段 --> 属性

2.模型需要继承自models.Model

3.模型会自动生成一个主键

4.格式：属性名 = models.属性类型（选项）
    属性名： 不要使用python、sql关键字
            不要使用连续下划线（__）
    属性类型：和mysql类型类似
    选项：  charfiled 必须设置max_length
                    相当于varchar(M)
            null 是否为空
            unique 唯一
            default 设置默认值
            verbose_name 主要是admin后台显示

"""
"""
书籍表：
    id, name, pub_data, readcount, commentcount, is_delete
"""
class BookInfo(models.Model):
    # 格式：属性名 = models.属性类型（选项）
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')
    pub_data = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    # 修改表名称
    class Meta:
        # 修改对象
        db_table = 'bookinfo'
        # 修改表名
        verbose_name = '哇哈哈'

    def __str__(self):
        return self.name

"""
人物信息表
"""
class PeopleInfo(models.Model):
    # 有序字典
    GENDER_CHOISE = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名字')
    gender = models.SmallIntegerField(choices=GENDER_CHOISE, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='书籍')
    # is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name


