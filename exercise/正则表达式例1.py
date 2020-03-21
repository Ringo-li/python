import re


def main():
    content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'
    regex = re.compile('\w*o\w*')
    y = regex.match(content)
    print(y)
    print(type(y))
    print(y.group())
    print(y.span())
    z = regex.findall(content)
    print(z)


if __name__ == '__main__':
    main()
# <_sre.SRE_Match object; span=(0, 5), match='Hello'>
# <class '_sre.SRE_Match'>
# Hello
# (0, 5)