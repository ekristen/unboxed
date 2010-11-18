import os
import mc

__id__ = "telnet"
__label__ = "Enable Telnet"
__description__ = "This will enable telnet on your Box, giving you full root access to the filesystem. There is one major caveat, there is no root password. It is advised you only enable telnet when you need to use it, then disable it."

def getlabel():
	status = mc.GetApp().GetLocalConfig().GetValue("telnettweak.status")
	if status == "0":
		return "Enable Telnet"
	else:
		return "Disable Telnet"

def onclick():
	status = mc.GetApp().GetLocalConfig().GetValue("telnettweak.status")
	if status == "0":
		start()
	else:
		stop()

def start():
	os.system("/etc/init.d/telnetd start")
	mc.GetApp().GetLocalConfig().SetValue("telnettweak.status", "1")
	ilist = mc.GetActiveWindow().GetList(101)
	item = ilist.GetItem(ilist.GetFocusedItem())
	item.SetLabel("Disable Telnet")
	mc.ShowDialogNotification("Telnet: Started")

def stop():
	os.system("/bin/kill `ps ax | grep -v grep | grep telnetd | awk '{print $1}'`")
	mc.GetApp().GetLocalConfig().SetValue("telnettweak.status", "0")
	ilist = mc.GetActiveWindow().GetList(101)
	item = ilist.GetItem(ilist.GetFocusedItem())
	item.SetLabel("Enable Telnet")
	mc.ShowDialogNotification("Telnet: Stopped")

def onload():
	return

def onunload():
	return

# Init Code Goes Below Here #
mc.GetApp().GetLocalConfig().SetValue("telnettweak.status", "0")
