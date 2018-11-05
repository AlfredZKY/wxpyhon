# -*- coding:utf-8 -*-
# Author:Alfred

import wx


# 自定义窗口类
class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent = None,title = "tool_bar",size = (400,200))

        # 窗口居中
        self.Center()

        # 创建一个编辑文本框
        self.text = wx.TextCtrl(self,-1,style = wx.EXPAND | wx.TE_MULTILINE)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 创建一个布局管理器
        vbox.Add(self.text,1,flag = wx.EXPAND | wx.ALL,border = 1)

        # 将布局管理器中添加控件
        self.SetSizer(vbox)

        # 创建菜单栏
        self.menubar = wx.MenuBar()

        # 创建菜单
        self.file_menu = wx.Menu()
        self.edit_menu = wx.Menu()

        # 创建新建菜单项
        new_item = wx.MenuItem(self.file_menu,wx.ID_NEW,text="新建",kind = wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU,self.on_newitem_click,id = wx.ID_NEW)

        # 将新建菜单项放入对应的菜单中
        self.file_menu.Append(new_item)
        self.file_menu.AppendSeparator()

        # 创建编辑菜单项
        copy_item = wx.MenuItem(self.file_menu,  1, text="拷贝", kind = wx.ITEM_NORMAL)
        cut_item = wx.MenuItem(self.file_menu,   2, text="剪切", kind = wx.ITEM_NORMAL)
        paste_item = wx.MenuItem(self.file_menu, 3, text="粘贴", kind = wx.ITEM_NORMAL)
        self.Bind(wx.EVT_MENU,self.on_edititem_click,id =1,id2=3)

        # 将编辑菜单项放入对应的菜单中
        self.edit_menu.Append(copy_item)
        self.edit_menu.AppendSeparator()
        self.edit_menu.Append(cut_item)
        self.edit_menu.AppendSeparator()
        self.edit_menu.Append(paste_item)
        self.edit_menu.AppendSeparator()



        # 将菜单项放入菜单栏中
        self.file_menu.Append(wx.ID_ANY, "编辑",self.edit_menu)
        self.menubar.Append(self.file_menu, "文件")


        # 将菜单栏放入顶层窗口中
        self.SetMenuBar(self.menubar)

        # 开始构建工具栏
        tb = wx.ToolBar(self,wx.ID_ANY)
        self.ToolBar = tb
        tsize = (24,24)

        # 创建系统在带的位图图片
        new_bmp = wx.ArtProvider.GetBitmap(wx.ART_NEW,wx.ART_TOOLBAR,tsize)
        open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize)
        copy_bmp = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR, tsize)
        past_bmp = wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_TOOLBAR, tsize)

        # 将位图图片添加到工具栏
        tb.AddTool(10, "New",   new_bmp,  kind = wx.ITEM_NORMAL, shortHelp = "New")
        tb.AddTool(20, "Open",  open_bmp, kind = wx.ITEM_NORMAL, shortHelp = "Open")
        tb.AddSeparator()
        tb.AddTool(30, "Copy",  copy_bmp, kind = wx.ITEM_NORMAL, shortHelp = "Copy")
        tb.AddTool(40, "Paste", past_bmp, kind = wx.ITEM_NORMAL, shortHelp = "Paste")
        tb.AddSeparator()

        # 创建自己的位图
        tb.AddTool(50, "Back", wx.Bitmap('menu_icon/back.png'), kind=wx.ITEM_NORMAL, shortHelp="Back")
        tb.AddTool(60, "Forward", wx.Bitmap('menu_icon/forward.png'), kind=wx.ITEM_NORMAL, shortHelp="Forward")

        # 显示出工具栏
        tb.Realize()




    def on_newitem_click(self,event):
        event.GetEventObject()
        source_id = event.GetId()
        self.text.SetLabel("单击{0},单击{1}".format(self.menubar.GetMenuLabel(0),self.file_menu.GetLabelText(source_id)))

    def on_edititem_click(self,event):
        source_id = event.GetId()
        if source_id == 1:
            self.text.SetLabel("单击copy菜单".format())
        elif source_id ==2:
            self.text.SetLabel("单击cut菜单".format())
        else:
            self.text.SetLabel("单击paste菜单".format())

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
