# -*- coding:utf-8 -*-
# Author:Alfred

import wx


# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None,title = "radir_and_check",size = (400,200))
        self.Center()

        # 创建面板
        panel = wx.Panel(self)

        # 首先画出三个水平box布局管理器
        hbox1 = wx.BoxSizer()
        hbox2 = wx.BoxSizer()
        hbox3 = wx.BoxSizer()
        hbox4 = wx.BoxSizer()
        hbox5 = wx.BoxSizer()
        hbox6 = wx.BoxSizer()

        # 一个垂直管理器
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 构建第一组数据
        static_text1 = wx.StaticText(panel,label = "选择你喜欢的语言：")
        cb1 = wx.CheckBox(panel,1,"python")
        cb2 = wx.CheckBox(panel, 2, "java")
        cb2.SetValue(True)
        cb3 = wx.CheckBox(panel, 3, "c")
        cb4 = wx.CheckBox(panel, 4, "c++")

        self.Bind(wx.EVT_CHECKBOX,self.on_checkbox_click,id =1,id2 =10)

        hbox1.Add(static_text1,1,flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE,border = 5)
        hbox2.Add(cb1, 1, flag=wx.ALL| wx.FIXED_MINSIZE)
        hbox2.Add(cb2, 1, flag=wx.ALL| wx.FIXED_MINSIZE)
        hbox2.Add(cb3, 1, flag=wx.ALL| wx.FIXED_MINSIZE)
        hbox2.Add(cb4, 1, flag=wx.ALL| wx.FIXED_MINSIZE)

        # 构建第二组数据
        static_text1 = wx.StaticText(panel, label="选择你喜欢吃得水果：")
        rb1 = wx.RadioButton(panel, 1, "香蕉",style = wx.RB_GROUP)
        rb2 = wx.RadioButton(panel, 2, "苹果")
        rb2.SetValue(True)
        rb3 = wx.RadioButton(panel, 3, "菠萝")
        rb4 = wx.RadioButton(panel, 4, "提子")

        self.Bind(wx.EVT_RADIOBUTTON,self.on_radio1_click,id=1,id2=10)
        hbox3.Add(static_text1, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox4.Add(rb1, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox4.Add(rb2, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox4.Add(rb3, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox4.Add(rb4, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        # 构建第三组数据
        static_text1 = wx.StaticText(panel, label="选择性别：")
        rb5 = wx.RadioButton(panel, 11, "男",style = wx.RB_GROUP)
        rb6 = wx.RadioButton(panel, 12, "女")
        rb5.SetValue(True)

        self.Bind(wx.EVT_RADIOBUTTON, self.on_radio2_click, id=11, id2=20)
        hbox5.Add(static_text1, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox6.Add(rb5, 1, flag=wx.ALL | wx.FIXED_MINSIZE)
        hbox6.Add(rb6, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        # 将水平管理放进垂直管理
        vbox.Add(hbox1, 1, flag = wx.ALL | wx.EXPAND, border = 5)
        vbox.Add(hbox2, 1, flag = wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox3, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox4, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox5, 1, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox6, 1, flag=wx.ALL | wx.EXPAND, border=5)
        # 面板显示
        panel.SetSizer(vbox)
    def on_checkbox_click(self,event):
        cb = event.GetEventObject()
        print('选择{0}，状态{1}'.format(cb.GetLabel(),event.IsChecked()))

    def on_radio1_click(self,event):
        rb = event.GetEventObject()
        print('选择{0}'.format(rb.GetLabel()))

    def on_radio2_click(self,event):
        rb = event.GetEventObject()
        print('选择{0}'.format(rb.GetLabel()))
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
