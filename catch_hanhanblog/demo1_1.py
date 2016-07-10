#-*-coding:utf-8*-*
import urllib
import re
import time
from multiprocessing import Process
from threading import Thread
import os


url='http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'

def parserHtml(url):

        html_list=[]
        html=urllib.urlopen(url).read()
        p=r'<a title=(.*?) href=(.*?)>'
        urls=re.findall(p,html)
        for i in urls:
                html_list.append(i[1].strip('"'))
        return html_list

def create_urls():
        url_list=[]
        for x in range(7):
                url_list.extend(parserHtml('http://blog.sina.com.cn/s/articlelist_1191258123_0_'+str(x+1)+'.html'))

        return url_list

def down_html(urls,dirpath):

        for url in urls:
                content=urllib.urlopen(url).read()
                if len(url)>0:
                        if not os.path.exists(dirpath):
                                os.makedirs(dirpath)
                        with open(dirpath+r'/'+url[-26:],'w') as f:
                                f.write(content)

def thread_process_job(n, Thread_or_Process, url_list, job):
        """
        n: 多线程或多进程数
        Thread_Process: Thread／Process类 
        job: countdown任务
        """
        local_time=time.time()
        threads_or_processes = [Thread_or_Process(target=job,args=(url_list[i],str(n)+Thread_or_Process.__name__)) for i in xrange(n)]
        for t in threads_or_processes:
                t.start()
        for t in threads_or_processes:
                t.join()

        print n,Thread_or_Process.__name__," run job need ",time.time()-local_time


if __name__=='__main__':

        urls=create_urls()
        for n in [8,4,2,1]:
                local_time=time.time
                url_list=[]
                url_split_len=len(urls)//n
                for i in range(n):
                        if i==n-1:
                                url_list.append(urls[i*url_split_len:len(urls)])
                        else:
                                url_list.append(urls[i*url_split_len:(i+1)*url_split_len])
                thread_process_job(n,Thread, url_list, down_html)
                thread_process_job(n,Process, url_list, down_html)
        