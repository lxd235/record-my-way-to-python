#! /usr/bin/env
# coding:utf-8
def readFile(filename):
	#读取字符
	fpath=open(filename,'r')
	y=[]
	row=fpath.readlines()
	for x in row:
		y.extend(x.split())
	fpath.close()

	# 单词格式化，去除不规则字符
	word_list=[]
	for word in y:
		word1=word
		char=[",",".",":",":",";",'"']
		while True:
			if word[-1] in char:
				word1=word.rstrip(word[-1])
				break
			else:
				break
		while True:
			if word1[0] in char:
				word1=word1.lstrip(word1[0])
				break
			else:
				break
		
		word_list.append(word1.lower())			 				

	word_freq=[]
	word_saved=[]
	for word in word_list:
		if word not in word_saved:
			word_saved.append(word)
			word_freq.append((word,word_list.count(word)))


	sorted_list = sorted(word_freq,key=lambda x:x[1],reverse=True)  
	return sorted_list		


#单词合并，输出单词词频表
def mergeword(list1,list2):
	word1,num1=zip(*list1)
	merge_list=[]
	for word,num in list2:
		if word not in word1:
			merge_list.append((word,num))
		else:
			index=word1.index(word)
			merge_list.append((word,num+num1[index]))
	word2,num2=zip(*list2)		
	for word3,num3 in list1:
		if word3 not in word2:
			merge_list.append((word3,num3))			

	sorted_list = sorted(merge_list,key=lambda x:x[1],reverse=True)    
	return sorted_list


if __name__=='__main__':
	filelist=['article_000.txt','article_001.txt','article_002.txt','article_003.txt','article_004.txt','article_005.txt'] 
	cc=map(readFile,filelist)
	results=[]
	results=reduce(mergeword,cc)
	
	print '最常用的单词排行榜为Top10：'
	for word in results[0:10]:
		print '%-10s%d'%(word[0],word[1])  

