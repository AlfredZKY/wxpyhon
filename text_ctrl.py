# -*- coding:utf-8 -*-
# Author:Alfred

import wx


# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None,title = "text_ctrl!!",size = (400,200))
        self.Center()

        # 画出面板
        panel = wx.Panel(self)

        # 画出三个静态文本作为标题
        userid = wx.StaticText(panel,label ="用户id:")
        pwd = wx.StaticText(panel, label="用户密码:")
        context = wx.StaticText(panel, label="多行内容")

        # 画出三个对应的文本框存放内容
        text_ct1 = wx.TextCtrl(panel)
        text_ct2 = wx.TextCtrl(panel,style = wx.TE_PASSWORD)
        text_ct3 = wx.TextCtrl(panel,style = wx.TE_MULTILINE)

        # 设置一个默认值
        text_ct1.SetValue("Tony")

        # 创建多行网格布局管理器
        flex_grid = wx.FlexGridSizer(3,2,10,10)

        # 向布局管理器中添加控件
        flex_grid.AddMany([
            userid,(text_ct1,1,wx.EXPAND),
            pwd, (text_ct2, 1, wx.EXPAND),
            context, (text_ct3, 1, wx.EXPAND)
        ])

        # 进行横竖位置调整
        flex_grid.AddGrowableCol(0, 1)
        flex_grid.AddGrowableCol(1, 2)

        flex_grid.AddGrowableRow(0, 1)
        flex_grid.AddGrowableRow(1, 1)
        flex_grid.AddGrowableRow(2, 3)

        # 增加一个垂直管理器box
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(flex_grid,1,flag = wx.ALL | wx.EXPAND, border = 10)

        # 面板进行显示
        panel.SetSizer(vbox)
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
