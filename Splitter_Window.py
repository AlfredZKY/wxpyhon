# -*- coding:utf-8 -*-
# Author:Alfred

import wx


# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None,title = "splitter_window",size = (400,200))
        self.Center()

        #  创建分割窗口对象
        splitter = wx.SplitterWindow(self,-1)

        # 创建左右面板
        leftpanel = wx.Panel(splitter)
        rightpanel = wx.Panel(splitter)

        # 将两个面板放入分割窗口的对象中
        splitter.SplitVertically(leftpanel,rightpanel,100)
        splitter.SetMinimumPaneSize(80)

        # 左边构建一个列表框
        list2 = ['苹果', '橘子', '香蕉']
        list_box = wx.ListBox(leftpanel,-1,choices = list2,style = wx.LB_SINGLE )
        self.Bind(wx.EVT_LISTBOX,self.on_listbox,list_box)

        # 构建垂直布局管理器
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(list_box,1,wx.ALL | wx.EXPAND,border = 5)
        leftpanel.SetSizer(vbox1)

        # 右边构建一个
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.context = wx.StaticText(rightpanel,label = "右侧面板")
        vbox2.Add(self.context,1,wx.ALL |wx.EXPAND,border = 5)
        rightpanel.SetSizer(vbox2)


    def on_listbox(self,event):
        s = '选择{0}'.format(event.GetString())
        self.context.SetLabel(s)



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
