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

        # 一个垂直管理器
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 构建第一组数据
        static_text1 = wx.StaticText(panel,label = "选择你喜欢的语言：")
        cb_list = ['python','java','c','c++']
        combobox = wx.ComboBox(panel,-1,value = 'c',choices = cb_list,style = wx.CB_SORT)

        self.Bind(wx.EVT_COMBOBOX,self.on_combobox_click,combobox)

        hbox1.Add(static_text1,1,flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE,border = 5)
        hbox1.Add(combobox, 1, flag=wx.ALL| wx.FIXED_MINSIZE)

        # 构建第二组数据
        static_text2 = wx.StaticText(panel, label="性别：")
        choice_list = ['男','女']
        ch = wx.Choice(panel, -1,choices = choice_list)
        ch.SetSelection(0)
        self.Bind(wx.EVT_CHOICE,self.on_choice_click,ch)
        hbox2.Add(static_text2, 1, flag=wx.LEFT | wx.RIGHT | wx.FIXED_MINSIZE, border=5)
        hbox2.Add(ch, 1, flag=wx.ALL | wx.FIXED_MINSIZE)

        # 将水平管理放进垂直管理
        vbox.Add(hbox1, 1, flag = wx.ALL | wx.EXPAND, border = 5)
        vbox.Add(hbox2, 1, flag=wx.ALL | wx.EXPAND, border=5)

        # 面板显示
        panel.SetSizer(vbox)

    def on_combobox_click(self,event):
        print('选择{0}'.format(event.GetString(),))

    def on_choice_click(self,event):
        print('选择{0}'.format(event.GetString(), ))

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
