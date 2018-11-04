# -*- coding:utf-8 -*-
# Author:Alfred

import wx


# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None,title = "listbox",size = (400,200))
        self.Center()

        # 创建面板
        panel = wx.Panel(self)

        # 创建两个水平布局管理器
        hbox1 = wx.BoxSizer()
        hbox1 = wx.BoxSizer()

        # 创建一个垂直布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 创建列表框
        statictext = wx.StaticText(panel, label='选择你喜欢的编程语言：')
        lb_list1 = ['Python', 'C++', 'Java']
        #lb1 = wx.ListBox(panel,-1,choices = lb_list1,style = wx.LB_MULTIPLE)
        lb1 = wx.ListBox(panel,-1,choices = lb_list1,style = wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX,self.on_listbox_click,lb1)

        hbox1.Add(statictext, 1,flag = wx.LEFT | wx.RIGHT |wx.FIXED_MINSIZE,border = 10)
        hbox1.Add(lb1,1,flag = wx.ALL | wx.FIXED_MINSIZE)


        vbox.Add(hbox1, 1 ,flag = wx.ALL | wx.EXPAND ,border = 5)

        panel.SetSizer(vbox)

    def on_listbox_click(self,event):
        listbox = event.GetEventObject()
        print("选择:{0}，语言:{1}".format(listbox.GetSelection(),event.GetString()))
        #print("选择:{0}，语言:{1}".format(listbox.GetSelections(),event.GetString()))

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