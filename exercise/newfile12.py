import os

a = os.getcwd()
print(a)


try:
	f = open("./test12.txt", 'w')
	f.write("hellow world")
except:
	pass
finally:
	f.close()

with open('./test12.sh', 'w') as file:
	file.write('hellow world')

    
    
