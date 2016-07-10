


# class listMetaClass(type):
#     def __new__(cls,name,bases,attrs):
#         print name,'calls',cls.__name__
#         attrs['add']=lambda self,value:self.append(value)
#         return type.__new__(cls,name,bases,attrs)
# class MyList(list):
#     __metaclass__=listMetaClass      



# a=MyList()    

class ModelMetaClass(type):
    def __new__(cls,name,bases,attrs):
        print 'name is ',name
        print 'bases is ',bases
        print "attrs is ",attrs        
class Model(dict):
    __metaclass__=ModelMetaClass    


