# -*- coding:utf-8 -*-
# Author:Alfred

import wx


# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None,title = "FlexGridSizer",size = (300,200))
        self.Center()

        # 创建面板
        panel = wx.Panel(parent = self)

        # 创建静态文本
        title = wx.StaticText(parent = panel,label = "标题")
        author = wx.StaticText(parent = panel,label = "作者名:")
        review = wx.StaticText(parent = panel,label = "内容")

        # 创建三个文本框
        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel,style = wx.TE_MULTILINE)

        # 创建FlexGridSizer布局
        fgs = wx.FlexGridSizer(3,2,10,10)

        # 将控件添加进布局管理器
        fgs.AddMany([
            title,(tc1,1,wx.EXPAND),
            author, (tc2, 1, wx.EXPAND),
            review, (tc3, 1, wx.EXPAND)
        ])

        # 进行位置调整
        fgs.AddGrowableRow(0,1)
        fgs.AddGrowableRow(1, 1)
        fgs.AddGrowableRow(2, 3)

        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableCol(1, 2)

        # 添加一个水平BoxSizer布局用于嵌套
        hbox = wx.BoxSizer()
        hbox.Add(fgs,proportion = 1,flag = wx.EXPAND |wx.ALL ,border=15)

        # 面板显示布局管理器
        panel.SetSizer(hbox)

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
