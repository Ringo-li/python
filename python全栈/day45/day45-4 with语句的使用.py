try:
    file = open("test.txt", "r")
    content = file.read()
    print(content)
except Exception as e:
    print(e)
finally:
    print("over")
    file.close()

with open("test.txt", "r") as file:
    content = file.read()
    print(content)