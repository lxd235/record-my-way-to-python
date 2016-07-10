#-*-coding:utf-8-*-
import time
from threading import Thread
from multiprocessing import Process


COUNT=100000000

def job(n):
        while n>0:
                n-=1


def thread_process(n,job,thr_or_pro):
        """
        n:多线程或多进程数量
        job:任务，函数类
        thr_or_pro:Process 或者Thread 类
        """
        #create thread or process
        pro_thread=[thr_or_pro(target=job,args=(COUNT//n,)) for x in range (n)]
        st_time=time.time()
        for a in pro_thread:
                a.start()
        for a in pro_thread:       
                a.join()
        print n,thr_or_pro.__name__,'cost time is :',time.time()-st_time

                
if __name__=='__main__':
        print 'the threading test:'
        for n in [1,2,4,8]:
                thread_process(n,job,Thread)

        print 'the threading test:'
        for n in [1,2,4]:
                thread_process(n,job,Process)