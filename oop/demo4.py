class Num(object):
	def __init__(self,x,y):
		self.x = float(x)
		self.y = float(y)
	def __add__(self,factor):
		return Num(self.x+factor.x,self.y+factor.y)
	def __str__(self):
		return "x={0},y={1}".format(self.x,self.y)
	@property
	def xy(self):
		return (self.x,self.y)	
	def __repr__(self):
		return str(self.xy)	
     

a=Num(20,30)
b=Num(30,40)
