# -*- coding:utf-8 -*-
# Author:Alfred

# -*- coding:utf-8 -*-
# Author:Alfred

import wx


# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None,title = "第一个GUI程序！",size = (400,200))
        self.Center()                       # 设置窗口居中
        panel = wx.Panel(parent = self)     # 在窗口中加入面板，父参数就是窗口实例
        self.statictext = wx.StaticText(parent = panel,pos = (160,20))
        b = wx.Button(parent = panel , label = "OK" ,pos = (150,40))
        self.Bind(wx.EVT_BUTTON, self.on_click,b)     #一对一进行事件绑定

    def on_click(self,event):
        print(type(event))
        self.statictext.SetLabelText("Hello world")


# 自定程序类
class App(wx.App):

    def OnInit(self):
        # 创建窗口对象
        frame = MyFrame()
        frame.Show()
        return True

    def OnExit(self):
        print("app exit")
        return 0


if __name__ == '__main__':
    app = App()
    app.MainLoop()
