#coding:utf-8
from flask import Flask,request,render_template



app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
        return  render_template('Home.html',name='zhoubo')

@app.route('/login',methods=['GET'])
def signin_form():
        return """<form action="/login" method="post">
                        <p><input name="username"></p>
                        <p><input name="password" type="password"></p>
                        <p><button type="submit">sign in</button></p>
                        </form>"""

@app.route('/login',methods=['POST'])
def chech():
        if request.form['username']=='admin' and request.form['password']=='password':
                return '<h3>hello,admin</h3>'
        return '<h3>bad username or password</h3>'




if __name__=='__main__':
        app.run()
