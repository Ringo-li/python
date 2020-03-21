text = open('test97.txt','r+')

text.write('hello\n,waha')
text.close()

a = open ('test97.txt','r') 
for i in a:
	print(i)
a.close()