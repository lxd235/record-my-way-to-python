import wx
app=wx.App()
frame=wx.Frame(None,-1,title='hello world',pos=(300,400))
frame.Show()
print 'hello,is me'
print 'what can i do for you?'
app.MainLoop()