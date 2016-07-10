# def extendList(val, list=[]):
#     list.append(val)
#     return list
# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a')
# print "list1 = %s" % list1
# print "list2 = %s" % list2
# print "list3 = %s" % list3

# list = ['a', 'b', 'c', 'd', 'e']
# print list[10:]


# def foo(val,a=[]):
#     a.append(val)
#     return a
# foo(2)
# foo(1,[])
# print foo.func_defaults
# foo(3)
# print foo.func_defaults

# def multipliers():
#     return [lambda x : i * x for i in range(4)]
# print [m(2) for m in multipliers()]
args=1
def foo(i=args):
    pass    

print foo.func_defaults
