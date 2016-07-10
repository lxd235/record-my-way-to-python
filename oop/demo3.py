class Car(object):
	name1='boss'
	__slots__=('age','name','dream','__dict__')
	def __init__(self,name,age,dream):
		self.name=name
		assert age>0,'age must larger than zero'
		self.age=age
		self.dream=dream
	def __getattr__(self,name):
		assert name in self.__slots__,'Not hava this attribute'+name
		print '__getattr__',name
		return self.__dict__.get(name,None)	
	def __setattr__(self,name,value):
		assert name in self.__slots__,'Not hava this attribute'+name
		print '__setattr__',name
		self.__dict__[name]=value
	def __delattr__(self,name):
		print '__delattr__',name
		self.__dict__[name]=None		
	 	
a=Car('zhoubo',1,'python')


