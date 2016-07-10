class A(object):
	a=1
	b=2
	def test(self):
		print "a'test"
class B(A):
	c=3
	def test(self):
		print "b'test"
		super(B,self).test()
class C(A):
	a=2
	b=3
	c=4
	def test(self):
		print "c'test"
		super(C,self).test()
class D(B,C):
	def test(self):
		print "d'test"
		super(D,self).test()

d=D()




