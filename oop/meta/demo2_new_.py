class listMetaClass(type):
    def __new__(cls,name,base,attrs):
        attrs['add']=lambda self,s:self.append(s)
        print name,cls,base,attrs
        return type.__new__(cls,name,base,attrs)  
 
class applist(list):
    __metaclass__=listMetaClass


L=applist()

