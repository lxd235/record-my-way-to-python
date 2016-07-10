
class Tmp(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __getattr__(self,name):
        print  '__getattr__:',name
        return  self.__dict__.get(name,None)

a=Tmp('zhoubo',25)
def f(self,value):
    return value**2
B=type('B',(object,),{'pow_2':f})
b=B()
print b.pow_2(4)




