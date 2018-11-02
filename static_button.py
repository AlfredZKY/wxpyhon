# -*- coding:utf-8 -*-
# Author:Alfred

import wx


# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None,title = "static and text！",size = (400,200),pos = (100,100))

        # 创建面板
        panel = wx.Panel(self)

        # 创建静态文本
        self.statictext = wx.StaticText(panel,label ="static text!")

        # 创建三个按钮
        b1 = wx.Button(panel,label = "ok")
        self.Bind(wx.EVT_BUTTON,self.on_click,b1)

        b2 = wx.ToggleButton(panel,-1, label="ToggleButton")
        self.Bind(wx.EVT_BUTTON, self.on_click, b2)

        # 创建图画的按钮
        bmp = wx.Bitmap('icon/1.png',wx.BITMAP_TYPE_PNG)
        b3 = wx.BitmapButton(panel,-1, bmp)
        self.Bind(wx.EVT_BUTTON, self.on_click, b3)

        # 将控件放进布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(100,10, proportion=1, flag=wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(self.statictext,proportion = -1,flag= wx.CENTER | wx.FIXED_MINSIZE)
        vbox.Add(b1, proportion=1, flag=wx.CENTER | wx.EXPAND | wx.FIXED_MINSIZE)
        vbox.Add(b2, proportion=1, flag=wx.CENTER | wx.EXPAND | wx.FIXED_MINSIZE)
        vbox.Add(b3, proportion=1, flag=wx.CENTER | wx.EXPAND | wx.FIXED_MINSIZE)

        # 面板显示布局管理器
        panel.SetSizer(vbox)

    def on_click(self,event):
        self.statictext.SetLabelText("hello world！！！")


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
