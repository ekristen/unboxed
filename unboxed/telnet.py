import os
import mc

__id__ = "telnet"
__label__ = "Enable Telnet"
__altlabel__ = "Disable Telnet"
__description__ = "This will enable telnet on your Box, giving you full root access to the filesystem. There is one major caveat, there is no root password. It is advised you only enable telnet when you need to use it, then disable it."

def onclick():
	status = check()
	if status == "0":
		start()
	else:
		stop()

def start():
	os.system("/etc/init.d/telnetd start")
	mc.GetApp().GetLocalConfig().SetValue("telnettweak.status", "1")
	ilist = mc.GetActiveWindow().GetList(101)
	item = ilist.GetItem(ilist.GetFocusedItem())
	item.SetLabel(__altlabel__)
	mc.ShowDialogNotification("Telnet: Started")

def stop():
	os.system("/bin/kill `ps ax | grep -v grep | grep telnetd | awk '{print $1}'`")
	mc.GetApp().GetLocalConfig().SetValue("telnettweak.status", "0")
	ilist = mc.GetActiveWindow().GetList(101)
	item = ilist.GetItem(ilist.GetFocusedItem())
	item.SetLabel(__label__)
	mc.ShowDialogNotification("Telnet: Stopped")

def check():
	return mc.GetApp().GetLocalConfig().GetValue("telnettweak.status")

def __label__():
	status = check()
	if status == "0":
		return __label__
	elif status == "1":
		return __altlabel__

def onload():
	status = check()
	if status == "0":
		ilist = mc.GetActiveWindow().GetList(101)
		item = ilist.GetItem(ilist.GetFocusedItem())
		item.SetLabel(__label__)
	else:
		ilist = mc.GetActiveWindow().GetList(101)
		item = ilist.GetItem(ilist.GetFocusedItem())
		item.SetLabel(__altlabel__)

# Init Code Goes Below Here #
mc.GetApp().GetLocalConfig().SetValue("telnettweak.status", "0")
