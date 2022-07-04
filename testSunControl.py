#!/usr/bin/env python
#
# Test SDL_Pi_SunControl
# John C. Shovic, SwitchDoc Labs
# April 27, 2017
#
#

#configuraton:
# Connect a Grove Cable from Grove I2C on SunControl to an I2C Port on Pi2Grover (Grove hat for the Raspberry Pi)
# Connect a Grove Cable from Grove USB Control on SunControl to  D21/D26 on Pi2Grover (Grove hat for the Raspberry Pi)

# imports

import sys
import time
import datetime
import random
import SDL_Pi_SunControl

# Main Program

print("")
print("Test SDL_Pi_SunControl Version 1.0 - SwitchDoc Labs")
print("")
print("Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S"))
print("")

# configuration

INA3221Address = 0x40

Pin_USBControlControl = 21
Pin_USBControlEnable = 26

Pin_WatchDog_Done = 13
Pin_WatchDog_Wake = 16

filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
starttime = datetime.datetime.utcnow()

sunControl = SDL_Pi_SunControl.SDL_Pi_SunControl(INA3221Address=INA3221Address, USBControlEnable=Pin_USBControlEnable, USBControlControl=Pin_USBControlControl, WatchDog_Done = Pin_WatchDog_Done, WatchDog_Wake=Pin_WatchDog_Wake)

while True:
    print("------------------------------")
    print("SunControl Voltages and Currents")
    print("------------------------------")

    # set Label
    myLabel = "LIPO_Battery"
    print("%s Load Voltage :\t  %3.2f V" % (myLabel, sunControl.readChannelVoltageV(SDL_Pi_SunControl.SunControl_LIPO_BATTERY_CHANNEL)))
    print("%s Current :\t\t  %3.2f mA" % (myLabel, sunControl.readChannelCurrentmA(SDL_Pi_SunControl.SunControl_LIPO_BATTERY_CHANNEL)))
    print()

    # set Label
    myLabel = "Solar Cell"
    print("%s Load Voltage :\t  %3.2f V" % (myLabel, sunControl.readChannelVoltageV(SDL_Pi_SunControl.SunControl_SOLAR_CELL_CHANNEL)))
    print("%s Current :\t\t  %3.2f mA" % (myLabel, sunControl.readChannelCurrentmA(SDL_Pi_SunControl.SunControl_SOLAR_CELL_CHANNEL)))
    print()

    # set Label
    myLabel = "Output"
    print("%s Load Voltage :\t\t  %3.2f V" % (myLabel, sunControl.readChannelVoltageV(SDL_Pi_SunControl.SunControl_OUTPUT_CHANNEL)))
    print("%s Current :\t\t  %3.2f mA" % (myLabel, sunControl.readChannelCurrentmA(SDL_Pi_SunControl.SunControl_OUTPUT_CHANNEL)))
    print()

    #
    time.sleep(2.0)

    # Turn the USB Power Off
    sunControl.setUSBControl(True)
    sunControl.setUSBEnable(True)
    sunControl.setUSBControl(False)

    print("------")
    print("USB Power turned OFF")
    print("------")

    time.sleep(5.0)

    # set Label
    print("------------------------------")
    print("SunControl Voltages and Currents")
    print("------------------------------")

    myLabel = "LIPO_Battery"

    print("%s Load Voltage :\t  %3.2f V" % (myLabel, sunControl.readChannelVoltageV(SDL_Pi_SunControl.SunControl_LIPO_BATTERY_CHANNEL)))
    print("%s Current :\t\t  %3.2f mA" % (myLabel, sunControl.readChannelCurrentmA(SDL_Pi_SunControl.SunControl_LIPO_BATTERY_CHANNEL)))
    print()

    # set Label
    myLabel = "Solar Cell"

    print("%s Load Voltage :\t  %3.2f V" % (myLabel, sunControl.readChannelVoltageV(SDL_Pi_SunControl.SunControl_SOLAR_CELL_CHANNEL)))
    print("%s Current :\t\t  %3.2f mA" % (myLabel, sunControl.readChannelCurrentmA(SDL_Pi_SunControl.SunControl_SOLAR_CELL_CHANNEL)))
    print()

    # set Label
    myLabel = "Output"

    print("%s Load Voltage :\t\t  %3.2f V" % (myLabel, sunControl.readChannelVoltageV(SDL_Pi_SunControl.SunControl_OUTPUT_CHANNEL)))
    print("%s Current :\t\t  %3.2f mA" % (myLabel, sunControl.readChannelCurrentmA(SDL_Pi_SunControl.SunControl_OUTPUT_CHANNEL)))

    time.sleep(2.0)

    print("------")
    print("USB Power turned ON")
    print("------")

    sunControl.setUSBControl(True)
    sunControl.setUSBEnable(True)

    time.sleep(5.0)
