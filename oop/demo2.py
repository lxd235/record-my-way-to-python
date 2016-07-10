class Car(object):
	name='boss'
	def __init__(self,name,age,dream):
		self.__name=name
		assert age>0,'age must larger than zero'
		self.__age=age
		self._dream=dream
	@property
	def name(self):
		return self.__name
		
	@name.setter
	def name(self,value):
		self.__name=value

	@name.deleter	
	def name(self):
		del self.__name	

	 	
a=Car('zhoubo',1,'python')
