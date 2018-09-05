#!/usr/bin/env python3
#############################################################################
# Filename    : PCF8591.py
# Description : ADC and DAC
# Author      : freenove
# modification: 2018/08/02
########################################################################
import smbus
import time
import RPi.GPIO as GPIO

ledPins = [11, 12, 13, 15, 16, 18, 22, 32, 36,40]
address = 0x48	#default address of PCF8591
bus=smbus.SMBus(1)
cmd=0x40		#command

def analogRead(chn):#read ADC value,chn:0,1,2,3
	value = bus.read_byte_data#!/usr/bin/env python3
#############################################################################
# Filename    : PCF8591.py
# Description : ADC and DAC
# Author      : freenove
# modification: 2018/08/02
########################################################################
import smbus
import time
import RPi.GPIO as GPIO

ledPins = [11, 12, 13, 15, 16, 18, 22, 32, 36,40]
address = 0x48    #default address of PCF8591
bus=smbus.SMBus(1)
cmd=0x40        #command

def analogRead(chn):#read ADC value,chn:0,1,2,3
    value = bus.read_byte_data(address,cmd+chn)
    return value
    
def analogWrite(value):#write DAC value
    bus.write_byte_data(address,cmd,value)    
    
def switch_led(ledtoswitch):
    for pin in ledPins:
        GPIO.output(pin, GPIO.HIGH) # Set all ledPins to high(+3.3V) to off led
    for x in ledPins:
        if ledtoswitch == x:
            GPIO.output(x,GPIO.LOW)
            

def loop():
    while True:
        value = analogRead(0)    #read the ADC value of channel 0
        analogWrite(value)        #write the DAC value
        voltage = value / 255.0 * 3.3  #calculate the voltage value
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        if (voltage > 0.15):
            switch_led(ledPins[0])
        if (voltage > 0.30):
            switch_led(ledPins[1])
        if (voltage > 0.45):
            switch_led(ledPins[2])
        if (voltage > 0.60):
            switch_led(ledPins[3])
        if (voltage > 0.75):
            switch_led(ledPins[4])
        if (voltage > 0.90):
            switch_led(ledPins[5])
        if (voltage > 1.05):
            switch_led(ledPins[6])
        if (voltage > 1.20):
            switch_led(ledPins[7])
        if (voltage > 1.35):
            switch_led(ledPins[8])
        if (voltage > 1.50):
            switch_led(ledPins[9])
      
        


def destroy():
    bus.close()
    for pin in ledPins:
        GPIO.output(pin, GPIO.HIGH) # Set all ledPins to high(+3.3V) to off led

def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    for pin in ledPins:
        GPIO.setup(pin, GPIO.OUT)   # Set all ledPins' mode is output
        GPIO.output(pin, GPIO.HIGH) # Set all ledPins to high(+3.3V) to off led
        
if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()
