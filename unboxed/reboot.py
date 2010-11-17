import mc
import os
from tweak import *

class RebootTweak(Tweak):
	name = "reboot"
	label = "Restart your Box"
	description = "Clicking this will prompt you to confirm you'd like to reboot your Box."
	def onclick(self):
		response = mc.ShowDialogConfirm("UnBoxed", "Are you sure you wish to reboot your box?", "No", "Yes")
		if response:
			os.system("/sbin/reboot")
		
reboot = RebootTweak()