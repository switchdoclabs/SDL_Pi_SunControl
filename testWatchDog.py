#!/usr/bin/env python
#
# Test SDL_Pi_SunControl
# SwitchDoc Labs
# April 27, 2017
#
#

# uses two Grove cables
# Standard Grove to Grove Cable from Grove WatchDog Plub on SunControl to D13/D16 on Pi2Grover Board
# Female Pin Header to Grove Cable Adaptor Cable (for WatchDog Out Pulse High Pin on SunControl Board)


# imports

import sys


import time
import datetime
import RPi.GPIO as GPIO

import SDL_Pi_SunControl

# Main Program

print ""
print "Test SDL_Pi_SunControl WatchDog Version 1.0 - SwitchDoc Labs"
print ""
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")
print ""

# configuration


# Grove connector from Grove WatchDog SunControl Board to Raspberry Pi (D13/D16 on Pi2Grover Board)
Pin_WatchDog_Done = 13
Pin_WatchDog_Wake = 16

Pin_WatchDog_Reset = 4



sunControl = SDL_Pi_SunControl.SDL_Pi_SunControl(WatchDog_Done=Pin_WatchDog_Done,  WatchDog_Wake=Pin_WatchDog_Wake)

sunControl.useWatchDog()

# Set Mode

# Mode = 0 -- Free Running WatchDog, no DONE signal Set - WatchDog Will Trigger
# Mode = 1 -- WatchDog Sent every 60 seconds (if you adjust WatchDog Addresses D0-D2 (Defaults to 64 seconds), then this will meed to be changed
Mode = 1

# Set up Two Interrupts on Wake and ResetPulseHigh (ResetN Open Drain pulses Low
def Wake_callback(pin):

	print "Pin=%i Wake Rising Pulse Detected: %s"% (pin, datetime.datetime.now().strftime("%H:%M:%S"))


def WatchDog_Reset_callback(pin):

	print "Pin=%i WatchDog Reset  Rising Pulse Detected: %s"% (pin, datetime.datetime.now().strftime("%H:%M:%S"))



GPIO.setup(Pin_WatchDog_Reset, GPIO.IN)


GPIO.add_event_detect(Pin_WatchDog_Wake, GPIO.RISING, callback=Wake_callback )  
GPIO.add_event_detect(Pin_WatchDog_Reset, GPIO.RISING, callback=WatchDog_Reset_callback )  

while True:

	# Free Running - Done every 64 seconds (default) and NO WAKE signal
	if (Mode == 0):
		print "--->"+datetime.datetime.now().strftime("%H:%M:%S")
		time.sleep(10.0);
	
	# Pat the Dog every 60 seconds
	if (Mode == 1):
		print "--->"+datetime.datetime.now().strftime("%H:%M:%S")
		sunControl.patTheWatchDog()
		print "WatchDog Patted"
		time.sleep(60);
	

