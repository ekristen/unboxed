import os
import mc
from tweak import *

# Let's define some tweaks
class TelnetTweak(Tweak):
	name = "telnet"
	label = "Enable Telnet"
	altlabel = "Disable Telnet"
	description = "This will enable telnet on your Box, giving you full root access to the filesystem. There is one major caveat, there is no root password. It is advised you only enable telnet when you need to use it, then disable it."

	def __init__(self):
		mc.GetApp().GetLocalConfig().SetValue("telnettweak.status", "0")

	def onload(self):
		status = self.check()
		if status == "0":
			ilist = mc.GetActiveWindow().GetList(101)
			item = ilist.GetItem(ilist.GetFocusedItem())
			item.SetLabel("Enable Telnet")
		else:
			ilist = mc.GetActiveWindow().GetList(101)
			item = ilist.GetItem(ilist.GetFocusedItem())
			item.SetLabel("Disable Telnet")

	def onclick(self):
		status = self.check()
		if status == "0":
			self.start()
		else:
			self.stop()

	def start(self):
		os.system("/etc/init.d/telnetd start")
		mc.GetApp().GetLocalConfig().SetValue("telnettweak.status", "1")
		ilist = mc.GetActiveWindow().GetList(101)
		item = ilist.GetItem(ilist.GetFocusedItem())
		item.SetLabel("Disable Telnet")
		mc.ShowDialogNotification("Telnet: Started")

	def stop(self):
		os.system("/bin/kill `ps ax | grep -v grep | grep telnetd | awk '{print $1}'`")
		mc.GetApp().GetLocalConfig().SetValue("telnettweak.status", "0")
		ilist = mc.GetActiveWindow().GetList(101)
		item = ilist.GetItem(ilist.GetFocusedItem())
		item.SetLabel("Enable Telnet")
		mc.ShowDialogNotification("Telnet: Stopped")

	def check(self):
		return mc.GetApp().GetLocalConfig().GetValue("telnettweak.status")

telnet = TelnetTweak()