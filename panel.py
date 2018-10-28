# -*- coding:utf-8 -*-
# Author:Alfred

# -*- coding:utf-8 -*-
# Author:Alfred

import wx


# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None,title = "第一个GUI程序！",size = (400,200),pos = (100,100))
        self.Center()                       # 设置窗口居中
        panel = wx.Panel(parent = self)     # 在窗口中加入面板，父参数就是窗口实例
        statictext = wx.StaticText(parent = panel,label = "hello world",pos = (10,10))

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
