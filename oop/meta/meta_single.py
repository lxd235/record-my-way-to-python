class singleModule(object):
    def __new__(cls):
        print cls
        if not hasattr(cls,'instance'):
            cls.instance=super(singleModule,cls).__new__(cls)
        return cls.instance
        

A=singleModule()
# B=singleModule()
