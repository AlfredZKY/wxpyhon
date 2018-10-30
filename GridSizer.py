# -*- coding:utf-8 -*-
# Author:Alfred

import wx

# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        # 初始化父类
        super().__init__(parent = None , title = "GridSizer",size = (300,300))
        self.Center()                           # 设置窗口居中
        panel = wx.Panel(parent = self)         # 设置一个面板，并绑定到窗口，窗口就是父参数

        # 创出9个按钮控件
        b1 = wx.Button(parent = panel, label = "1")
        b2 = wx.Button(parent = panel, label = "2")
        b3 = wx.Button(parent = panel, label = "3")
        b4 = wx.Button(parent = panel, label = "4")
        b5 = wx.Button(parent = panel, label = "5")
        b6 = wx.Button(parent = panel, label = "6")
        b7 = wx.Button(parent = panel, label = "7")
        b8 = wx.Button(parent = panel, label = "8")
        b9 = wx.Button(parent = panel, label = "9")

        # 创建 GridSizer
        grid = wx.GridSizer(cols = 3, rows= 3,vgap = 3, hgap = 3)

        # 将按钮控件放进布局管理器中
        grid.AddMany([
            (b1, 0, wx.EXPAND),
            (b2, 0, wx.EXPAND),
            (b3, 0, wx.EXPAND),
            (b4, 0, wx.EXPAND),
            (b5, 0, wx.EXPAND),
            (b6, 0, wx.EXPAND),
            (b7, 0, wx.EXPAND),
            (b8, 0, wx.EXPAND),
            (b9, 0, wx.EXPAND)
            ]
        )
        # grid.Add(b1,0,wx.EXPAND)
        # grid.Add(b2, 0, wx.EXPAND)
        # grid.Add(b3, 0, wx.EXPAND)
        # grid.Add(b4, 0, wx.EXPAND)
        # grid.Add(b5, 0, wx.EXPAND)
        # grid.Add(b6, 0, wx.EXPAND)
        # grid.Add(b7, 0, wx.EXPAND)
        # grid.Add(b8, 0, wx.EXPAND)
        # grid.Add(b9, 0, wx.EXPAND)
        # 最后一定要把管理器设置到面板中
        panel.SetSizer(grid)



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