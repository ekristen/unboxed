import mc
import os

__id__ = "logo"
__label__ = "Toggle Box Logo"
__description__ = "Toggle through the different optons for the Boxee Logo on the Box. Options are Green, Red, and Off"

def onclick():
	state = mc.GetApp().GetLocalConfig().GetValue("logotweak.state")
		
	if state == "green":
		#red
		os.system('printf "\xAA\x06\x35\x30\x30\x33\x30\x30\x35\x33" > /dev/ttyS1')
		os.system('printf "\xAA\x06\x35\x30\x30\x31\x36\x34\x42\x35" > /dev/ttyS1')
		mc.GetApp().GetLocalConfig().SetValue("logotweak.state", "red")
		mc.ShowDialogNotification("Boxee Box Logo: Red")
	elif state == "red":
		#off
		os.system('printf "\xAA\x06\x35\x30\x30\x33\x30\x30\x35\x33" > /dev/ttyS1')
		mc.GetApp().GetLocalConfig().SetValue("logotweak.state", "off")
		mc.ShowDialogNotification("Boxee Box Logo: Off")
	elif state == "off":
		#green
		os.system('printf "\xAA\x06\x35\x30\x30\x33\x30\x30\x35\x33" > /dev/ttyS1')
		os.system('printf "\xAA\x06\x35\x30\x30\x32\x36\x34\x42\x36" > /dev/ttyS1')
		mc.GetApp().GetLocalConfig().SetValue("logotweak.state", "green")
		mc.ShowDialogNotification("Boxee Box Logo: Green")

def onload():
	return
	
def onunload():
	return

## Init Code Goes Below Here ##
mc.GetApp().GetLocalConfig().SetValue("logotweak.state", "green")
