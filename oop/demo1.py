#coding:utf-8

class A:
	"""This is class A"""
	country=u'中国'

class B(object):
	"""this is class B"""
	country=u'中国'
	#__slots__ = ('x','y')
	def __init__(self,name,age):
		self.__name = name
		self.__age = age
	def __getattr__(self,name):
		print 'get ',name
		return self.__dict__.get(name,None)	
	def medth(self):
		print 'hello world'

a=A()
b=B('zhoubo',25)



class Tmp(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
	@property	
	def xy(self):
		return (self.x,self.y)	
	def __repr__(self):
		return str(self.xy)

c=Tmp(10,10)
		