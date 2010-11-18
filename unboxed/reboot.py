import mc
import os

__id__ = "reboot"
__label__ = "Restart your Box"
__description__ = "Clicking this will prompt you to confirm you'd like to reboot your Box."

def onclick():
	response = mc.ShowDialogConfirm("UnBoxed", "Are you sure you wish to reboot your box?", "No", "Yes")
	if response:
		os.system("/sbin/reboot")

def getlabel():
	return __label__

def onload():
	return

def onunload():
	return

# Init Code Goes Below This Point #