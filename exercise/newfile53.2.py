class Singleton():
#	instance = None
#	def __new__(cls,*args,**kwargs):
#		if cls.instance is None:
#			cls.instance = super().__new__(cls)
#		return cls.instance
		
	def __new__(cls,*args,**kwargs):
		instance = super().__new__(cls)
		return instance

a = Singleton('nihao')
b = Singleton('hello')	
print(id(a))
print(id(b))
