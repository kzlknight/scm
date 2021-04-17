_复制代码_ 代码如下:

  
import wx  
import images  
class DemoTaskBarIcon(wx.TaskBarIcon):  
TBMENU_RESTORE = wx.NewId()  
TBMENU_CLOSE = wx.NewId()  
TBMENU_CHANGE = wx.NewId()  
TBMENU_REMOVE = wx.NewId()  
  
def __init__(self, frame):  
wx.TaskBarIcon.__init__(self)  
self.frame = frame

# Set the image  
icon = self.MakeIcon(images.getWXPdemoImage())  
self.SetIcon(icon, "wxPython Demo")  
self.imgidx = 1  
  
# bind some events  
self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarActivate)  
self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, id=self.TBMENU_RESTORE)  
self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=self.TBMENU_CLOSE)  
self.Bind(wx.EVT_MENU, self.OnTaskBarChange, id=self.TBMENU_CHANGE)  
self.Bind(wx.EVT_MENU, self.OnTaskBarRemove, id=self.TBMENU_REMOVE)

  
def CreatePopupMenu(self):  
"""  
This method is called by the base class when it needs to popup  
the menu for the default EVT_RIGHT_DOWN event. Just create  
the menu how you want it and return it from this function,  
the base class takes care of the rest.  
"""  
menu = wx.Menu()  
menu.Append(self.TBMENU_RESTORE, "Restore wxPython Demo")  
menu.Append(self.TBMENU_CLOSE, "Close wxPython Demo")  
menu.AppendSeparator()  
menu.Append(self.TBMENU_CHANGE, "Change the TB Icon")  
menu.Append(self.TBMENU_REMOVE, "Remove the TB Icon")  
return menu

  
def MakeIcon(self, img):  
"""  
The various platforms have different requirements for the  
icon size...  
"""  
if "wxMSW" in wx.PlatformInfo:  
img = img.Scale(16, 16)  
elif "wxGTK" in wx.PlatformInfo:  
img = img.Scale(22, 22)  
# wxMac can be any size upto 128x128, so leave the source img alone....  
icon = wx.IconFromBitmap(img.ConvertToBitmap() )  
return icon  

def OnTaskBarActivate(self, evt):  
if self.frame.IsIconized():  
self.frame.Iconize(False)  
if not self.frame.IsShown():  
self.frame.Show(True)  
self.frame.Raise()

  
def OnTaskBarClose(self, evt):  
self.frame.Close()

  
def OnTaskBarChange(self, evt):  
names = [ "WXPdemo", "Mondrian", "Pencil", "Carrot" ]  
name = names[self.imgidx]  
  
getFunc = getattr(images, "get%sImage" % name)  
self.imgidx += 1  
if self.imgidx >= len(names):  
self.imgidx = 0  
  
icon = self.MakeIcon(getFunc())  
self.SetIcon(icon, "This is a new icon: " + name)

  
def OnTaskBarRemove(self, evt):  
self.RemoveIcon()

  
class MyFrame(wx.Frame):

def __init__(self):  
wx.Frame.__init__(self, None, -1, "My Frame", size=(300, 300))  
panel = wx.Panel(self, -1)  
panel.Bind(wx.EVT_MOTION, self.OnMove)  
wx.StaticText(panel, -1, "Pos:", pos=(10, 12))  
self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))  
  
try:  
self.tbicon = DemoTaskBarIcon(self)  
except:  
self.tbicon = None  
  
#wx.CallAfter(self.ShowTip)  
  
#self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)  
#self.Bind(wx.EVT_ICONIZE, self.OnIconfiy)  
def OnCloseWindow(self, event):  
self.dying = True  
self.demoPage = None  
self.codePage = None  
self.mainmenu = None  
if self.tbicon is not None:  
self.tbicon.Destroy()  
self.Destroy()  
def OnIconfiy(self, evt):  
wx.LogMessage("OnIconfiy: %s" % evt.Iconized())  
evt.Skip()  
def OnMove(self, event):  
pos = event.GetPosition()  
self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

if __name__ == '__main__':  
app = wx.PySimpleApp()  
frame = MyFrame()  
frame.Show(True)  
app.MainLoop()  

