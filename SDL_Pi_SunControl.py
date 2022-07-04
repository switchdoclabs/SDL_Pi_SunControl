#!/usr/bin/env python

# SDL_Pi_SunControl.py Python Driver Code
# SwitchDoc Labs July 2017
# V 1.2

# imports

import sys
sys.path.append('./SDL_Pi_INA3221')

import time
import datetime
import random
import SDL_Pi_INA3221

import RPi.GPIO as GPIO

# constants
SunControl_INA3221Address       = 0x40
SunControl_USBControlEnable     = 26
SunControl_USBControlControl    = 21

# the three channels of the INA3221 named for SunAirPlus Solar Power Controller channels (www.switchdoc.com)
SunControl_LIPO_BATTERY_CHANNEL = 1
SunControl_SOLAR_CELL_CHANNEL   = 2
SunControl_OUTPUT_CHANNEL       = 3

# WatchDog Values
SunControl_WatchDog_Done = 13
SunControl_WatchDog_Wake = 16
SunControl_WatchDog_Use = False

class SDL_Pi_SunControl():

    ###########################
    # SunControl Code
    ###########################
    def __init__(self, INA3221Address=SunControl_INA3221Address, USBControlEnable=SunControl_USBControlEnable, USBControlControl=SunControl_USBControlControl, WatchDog_Use=SunControl_WatchDog_Use, WatchDog_Done=SunControl_WatchDog_Done, WatchDog_Wake=SunControl_WatchDog_Wake):
        self._INA3221Address = INA3221Address
        self._USBControlEnable = USBControlEnable
        self._USBControlControl = USBControlControl
        self._WatchDog_Done = WatchDog_Done
        self._WatchDog_Wake = WatchDog_Wake
        self._WatchDog_Use = WatchDog_Use
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        # defaults to battery voltage control (Enable = 0 for Bat Volt Control)
        GPIO.setup(self._USBControlEnable, GPIO.OUT, initial=False)
        GPIO.setup(self._USBControlControl, GPIO.OUT, initial=False)
        if (self._WatchDog_Use):
            GPIO.setup(self._WatchDog_Done, GPIO.OUT, initial=False)
            GPIO.setup(self._WatchDog_Wake, GPIO.IN)
        self._ina3221 = SDL_Pi_INA3221.SDL_Pi_INA3221(addr=self._INA3221Address)

    # public functions

    ##########################
    # INA3221 Three Channel ADC
    ##########################

    def readChannelVoltageV(self, channel):
        busvoltage1 = self._ina3221.getBusVoltage_V(channel)
        shuntvoltage1 = self._ina3221.getShuntVoltage_mV(channel)
        loadvoltage1 = busvoltage1 + (shuntvoltage1 / 1000)
        return loadvoltage1

    def readChannelCurrentmA(self, channel):
        current_mA1 = self._ina3221.getCurrent_mA(channel)
        return current_mA1

    ##########################
    # USBPowerControl
    ##########################

    def setUSBEnable(self, value):
        GPIO.output(self._USBControlEnable, value)
        return value

    def setUSBControl(self, value):
        GPIO.output(self._USBControlControl, value)
        return value

    ##########################
    # WatchDog
    ##########################

    def useWatchDog(self):
        self._WatchDog_Use = True
        GPIO.setup(self._WatchDog_Done, GPIO.OUT, initial=False)
        GPIO.setup(self._WatchDog_Wake, GPIO.IN)

    def patTheWatchDog(self):
        GPIO.output(self._WatchDog_Done, True)
        time.sleep(0.000100)
        GPIO.output(self._WatchDog_Done, False)
