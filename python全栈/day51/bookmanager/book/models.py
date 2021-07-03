from django.db import models

# Create your models here.
"""
1.定义模型表
2.模型迁移
    2.1先生成迁移文件（不会在数据库中生成表，只会创建一个和数据库的对应关系）
    python3 manage.py makemigrations
    2.2再迁移（会在数据库中生产表）
    python3 manage.py migrate
3.操作数据库

在哪里定义模型
模型继承与谁
orm对应关系
    表--类
    字段--属性
ORM:Object Relational Mapping
"""
class BookInfo(models.Model):
    """
    1.主键 当前会自动生成
    2.属性复制过来就可以
    """
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

