alist = [2,3,5,4,9,6]
print(alist)

#a = int(input('first num:'))
#b = int(input('second num:'))

#print(str(a)+'+'+str(b)+'=',a+b)
print(sorted(alist))
print('alist is :',alist)

new_list = []
def get_min(list):
	a = min(list)
	list.remove(a)
	new_list.append(a)
	if len(list) > 0:
		get_min(list)
	return new_list
	
blist = get_min(alist)
print(blist)
blist.sort(reverse=1)
print(blist)



 
