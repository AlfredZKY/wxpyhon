# -*- coding:utf-8 -*-
# Author:Alfred

# -*- coding:utf-8 -*-
# Author:Alfred

import wx


# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None,title = "鼠标事件",size = (400,200))
        self.Center()                       # 设置窗口居中
        # panel = wx.Panel(parent = self)     # 在窗口中加入面板，父参数就是窗口实例

        # 对于鼠标来说，事件源和事件处理者都是一个对象可能是窗口或者面板
        # 绑定鼠标事件 鼠标左键按下 抬起 和 按下移动事件
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.Bind(wx.EVT_MOTION, self.on_move)

    def on_left_down(self,event):
        print("鼠标左键按下")

    def on_left_up(self,event):
        print("鼠标左键抬起")

    def on_move(self, event):
        if event.Dragging() and event.LeftIsDown():
            pos = event.GetPosition()
            print("鼠标左键并移动:%s" % pos)

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


