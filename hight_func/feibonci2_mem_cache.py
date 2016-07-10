# import random
# mem_cache={}
# def feibo(n):
# 	if n not in mem_cache.keys():
# 		if n<=2:
# 			mem_cache[n]=1
# 		else:
# 			mem_cache[n]=feibo(n-1)+feibo(n-2)
# 	return mem_cache[n]
# print feibo(10)
# print mem_cache				

def feibo(n):
    a,b,i = 0,1,0
    while i<n:
        a,b = b,a+b
        i+=1
    return b
print feibo(10)