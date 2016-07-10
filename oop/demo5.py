class Employee(object):
	def __init__(self,name,job,salary):
		self.name=name
		self.job=job
		self.salary=salary
	def raiseSalary(self,pencent):
		self.salary=self.salary*(1+pencent)
	def __str__(self):
		return 'name:%3s job:%3s salary:%3s'%(self.name,self.job,self.salary)	

class Manager(Employee):
	def __init__(self,name,salary):
		#Employee.__init__(self,name,'mg',salary)
		super(Manager,self).__init__(name,'mg',salary)
	def raiseSalary(self,pencent,bonus=0.1):
		#Employee.raiseSalary(self,pencent+bonus)
		super(Manager,self).raiseSalary(pencent+bonus)	


a=Employee('lisi','teacher',5000)
b=Employee('liubei','emperor',20000)
c=Manager('zhoubo',15000)

if __name__=='__main__':
	mumbers=[a,b,c]
	for ob in mumbers:
		ob.raiseSalary(0.10)
		print ob
