#我以为的函数达不到目的
def fn(k,v):
	dic = {}
	dic[k] = v
	print(dic)
	
fn('haha',3)
fn('hello',2)

class dicfn():
	dic = {}
	def fn(self,k,v):
		self.dic[k] = v
		return self.dic
		
a = dicfn()
print(a.fn('haha',2))
print(a.fn('hello',3))
b = dicfn()
print(b.fn('hi',1))

def 
