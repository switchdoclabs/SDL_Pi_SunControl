SunControl Raspberry Pi Python Libraries
SwitchDoc Labs
www.switchdoc.com

## Installation:
#### Necessary Packages:
```
sudo apt install raspi-config python3-pip i2c-tools
```
```
pip install smbus
```
#### Configure Raspberry Pi to use I2C:
```
sudo raspi-config
```
Interfacing Options -> I2C -> Yes -> Ok -> Finish
#### Test SunControl:
```
python testSunControl.py
```
