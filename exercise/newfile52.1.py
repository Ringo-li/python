#alist = [2,9,5,3,1,8,6,7,4,9,6]
#print('原列表',alist)
#alist.sort()
#print('sort改变了原列表',alist)
blist = [2,9,5,3]
#clist = sorted(blist)
#print('sorted不改变原列表',blist)
#print('新列表',clist)
new = []
def change(alist):
	def getmin():
		a = min(alist)
		alist.remove(a)
		new.append(a)
	getmin()
	if len(alist) > 0:
		change(alist)
	return new	
print(change(blist))


blist = [2,6,8,5]
newlist = []
def get_min(alist):
#	print('old list',alist)
	a = min(alist)
	alist.remove(a)
#	print(blist)
	newlist.append(a)
	if len(alist) > 0:
		get_min(alist)
	return newlist
	
b = get_min(blist)
print(b)
	
	