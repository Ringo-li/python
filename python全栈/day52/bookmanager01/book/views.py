from django.shortcuts import render
from book.models import BookInfo, PeopleInfo
# Create your views here.

def add(request):
    # 1.方法一
    # 1.1先新增数据。
    people = PeopleInfo(
        name = '任我行',
        description = '任性',
        book_id = '4',
        gender = 1
    )
    # 1.2调用save方法
    people.save()

    # 2.方法二
    # 直接入库
    PeopleInfo.objects.create(
        name = '鳌拜',
        description = '霸蛮',
        book_id = '3',
        gender = 1

    )
    peoples = PeopleInfo.objects.all()
    context = {
        'peoples': peoples
    }
    # 3.传递给模板
    return render(request, 'people.html', context)

"""
类似于 ipython：
python3 manage.py shell
"""

# #####################更新数据######################
def update(request):
    # 1.数据库中查询书籍数据
    books = BookInfo.objects.all()

    # 2.组织数据
    # 2.1方法一
    # 2.1.1先查询数据
    # select * from bookinfo where id=1
    book = BookInfo.objects.get(id=1)
    # 2.2.1直接修改实例的属性
    book.readcount = 15214
    # 2.3.1调用save方法
    book.save()

    # 2.2方法二
    # filter过滤
    BookInfo.objects.filter(id=1).update(
        readcount = 15215,
        commentcount = 243,
    )


    context = {
        'books': books
    }
    # 3.传递给模板
    return render(request, 'book.html', context)

# #####################删除数据######################
def delete(request):
    # 2.组织数据
    # 2.1方法一
    # 2.1.1先查询数据
    # select * from peopleinfo where name='鳌拜'
    people = PeopleInfo.objects.get(name='鳌拜')
    # 2.2.1调用删除方法
    people.delete()
    # 2.3.1不需要调用save方法

    # 2.2方法二
    # filter过滤
    PeopleInfo.objects.filter(name='任我行').delete()
    # 1.数据库中查询人物数据
    peoples = PeopleInfo.objects.all()
    context = {
        'peoples': peoples
    }
    # 3.传递给模板
    return render(request, 'people.html', context)


# 查询description中包含'正'字的name
# PeopleInfo.objects.all().filter(description__contains='正')
# PeopleInfo.objects.all().filter(description__contains='正')[0].description