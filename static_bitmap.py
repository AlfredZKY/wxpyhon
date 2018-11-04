# -*- coding:utf-8 -*-
# Author:Alfred

import wx


# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None,title = "static_bitmap",size = (400,200))
        self.Center()

        # 构建位图列表
        self.bmp = [wx.Bitmap('images/bird3.gif', wx.BITMAP_TYPE_GIF),
                    wx.Bitmap('images/bird4.gif', wx.BITMAP_TYPE_GIF),
                    wx.Bitmap('images/bird5.gif', wx.BITMAP_TYPE_GIF)]
        # 创建面板
        self.panel = wx.Panel(self)

        # 创建布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 创建静态控件和按钮控件
        b1 = wx.Button(self.panel, 1 ,label = "按钮1")
        b2 = wx.Button(self.panel, 2, label="按钮2")
        self.sb = wx.StaticBitmap(self.panel,-1,self.bmp[0])

        # 进行按钮控件和事件处理函数进行绑定
        self.Bind(wx.EVT_BUTTON,self.on_button_down,id =1,id2=2)

        # 把控件放进布局管理器
        vbox.Add(b1, 1, wx.ALL | wx.CENTER | wx.EXPAND | wx.FIXED_MINSIZE)
        vbox.Add(b2, 1, wx.ALL | wx.CENTER | wx.EXPAND | wx.FIXED_MINSIZE)
        vbox.Add(self.sb, 3, wx.ALL | wx.CENTER | wx.EXPAND | wx.FIXED_MINSIZE)

        # 面板显示出布局管理器
        self.panel.SetSizer(vbox)

    def on_button_down(self,event):
        source_id = event.GetId()
        if source_id == 1:
            self.sb.SetBitmap(self.bmp[1])
        else:
            self.sb.SetBitmap(self.bmp[2])

        # 进行窗口刷新
        self.panel.Layout()
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
