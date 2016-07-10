#coding:utf-8




def application(dic,start_response):
        start_response('200 ok',[('Content-Type','text/html')])

        return '<h1>Hello,%s<h1>'%(dic['PATH_INFO'][1:] or 'web')
