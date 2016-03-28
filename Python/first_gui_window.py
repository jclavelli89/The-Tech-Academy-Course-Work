import wx

app = wx.App() # all wx python must have this

frame = wx.Frame(None, -1, 'Window Title', style = wx.MAXIMIZE_BOX | wx.SYSTEM_MENU
                 | wx.CAPTION )
frame.Show()

app.MainLoop()

