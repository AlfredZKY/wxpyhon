# -*- coding:utf-8 -*-
# Author:Alfred

import wx

# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        # 初始化父类
        super().__init__(parent = None , title = "first GUI 程序！",size = (300,120))
        self.Center()                           # 设置窗口居中
        panel = wx.Panel(parent = self)         # 设置一个面板，并绑定到窗口，窗口就是父参数

        # 设置一个垂直方向的box布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 设置一个水平方向的box布局管理器
        hbox = wx.BoxSizer()  # 默认就是水平方向的

        self.statictext = wx.StaticText(parent=panel, label="hello world")

        # 将静态文本加入到垂直管理器中
        vbox.Add(self.statictext,proportion = 2,flag = wx.FIXED_MINSIZE | wx.TOP | wx.CENTER ,border = 10 )

        # 画出两个按钮
        b1 = wx.Button(parent = panel, id = 10, label = "button1")
        b2 = wx.Button(parent = panel, id = 11, label = "button2")

        # 将两个按钮和面板绑定并绑定事件处理函数
        self.Bind(wx.EVT_BUTTON,self.on_click,id = 10 ,id2 = 20 )

        # 将两个按钮绑定到水平布局管理器中
        hbox.Add(b1, proportion = 0, flag = wx.BOTTOM | wx.EXPAND, border = 5)
        hbox.Add(b2, proportion = 0, flag = wx.BOTTOM | wx.EXPAND, border = 5)

        # 将水平管理器添加到垂直管理器中
        vbox.Add(hbox,proportion = 1,flag = wx.CENTER)

        # 最后一定要把管理器设置到面板中
        panel.SetSizer(vbox)

    def on_click(self,event):
        source_id = event.GetId()
        print(source_id)
        if source_id == 10:
            print("click button1")
            self.statictext.SetLabelText("click button1")
        else:
            print("click button2")
            self.statictext.SetLabelText("click button2")


# 自定义应用程序类
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