import csv
import re
def readFile(filename):
	fpath=open(filename,'r')
	reader=csv.reader(fpath)
	reader.next()
	result={}
	while True :
		loops+=1
		try:
			jt_info=reader.next()
		except:
			break
		
		stations_list=[]	
		pattern=(r'(?P<number>[0-9]+)\s(?P<stations>\D+)')
		stations=re.findall(pattern,jt_info[-1].decode('utf-8'))
		for row in stations:
			stations_list.append(row[1].strip())

		result[jt_info[1]]=stations_list	

	fpath.close()	
	return result
if __name__=='__main__':
	for i,k in readFile('beijing_jt.csv').iteritems():
		print i.decode('utf-8')
		for x in k:
			print x
		