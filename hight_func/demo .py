# coding:utf-8
import random
lower=lambda x,y:x if x<y else y
print lower(0,-1)
print '######################'
lis=[random.randint(-50,50) for x in range(100)]
print filter(lambda x:x>0,lis)
print filter(lambda x:not x%2,lis)
print map(lambda x: x**2,lis)
print reduce(lambda x,y:x+y,lis)

a='aabbccddAKUYIGKlikrlir02312DSAASDSBBCAS13'
lis=list(filter(str.isalpha,a))
newlis=sorted(lis,cmp=lambda x,y: -1 if (x.upper()>y.upper())else 1)
print newlis


print '######################'

def pow_x(x):
	def echo(value):
		return value**x
	return echo
	
lst=[pow_x(i) for i in range(1,5)]
for func in lst:
        print func(2)
		
def decorator(func):
	print 'func:%s is called'%func.__name__
	return func

@decorator
def func():
	print 'func is run'


#func()
import time
def time_cost(timef,loops):
	def decorator(test_f):
		def deco(*arg,**args):
			time_sum=0.0
			min_time=0.0
			for x in range(loops):
				st_time=timef()
				a=test_f(*arg,**args)
				ed_time=timef()
				time_sum +=ed_time-st_time
			print '%s aver run time is %f'%(test_f.__name__,time_sum/loops)
			return a
		return deco
	return decorator	

@time_cost(time.clock,10)
def for_list(length):
	return [(x,y) for x in range(length) for y in range(length) if x*y>25]

@time_cost(time.clock,10)
def two_for(length):
	a=[]
	for x in range(length):
		for y in range(length):
			if x*y>25:
				a.append((x,y))
	return a			



def feibo(n):
	if n<=2:
		return 1
	else :
		return feibo(n-1)+feibo(n-2)
#斐波拉茨
#print [feibo(i) for i in range(20)]

def reverse(s):
	if len(s)<=1:
		return s
	else:
		return reverse(s[1:])+s[0]
print reverse('ilikepython')

def fib_opt(n):
	a,b,i=0,1,0
	while i<n:
		a,b=b,a+b
		i+=1
	return b

def fib_iter():
	a,b=0,1
	while True:
		yield b
		a,b=b,a+b
st=time.clock()
fib0=[fib_opt(i) for i in range(1000) ]
ed=time.clock()
print 'fib_opt time is:',st-ed
print '#################################'
a=fib_iter()
st=time.clock()
fib1=[a.next() for i in range(1000)]		
ed=time.clock()
print 'fib_iter time is:',st-ed
