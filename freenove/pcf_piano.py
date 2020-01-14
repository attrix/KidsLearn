#!/usr/bin/env python3
#############################################################################
# Filename    : PCF8591.py
# Description : ADC and DAC
# Author      : freenove
# modification: 2018/08/02
########################################################################
import smbus
import time
import math
import RPi.GPIO as GPIO

ledPins = [11, 12, 13, 15, 16, 18, 22, 32, 36,40]
buzzerPin = 29
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
        #print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        if (voltage > 3.2):
            alertor(500)
            switch_led(ledPins[9])
        elif (voltage > 2.90):
            alertor(1000)
            switch_led(ledPins[8])
        elif (voltage > 2.50):
            alertor(1500)
            switch_led(ledPins[7])
        elif (voltage > 2.20):
            alertor(2000)
            switch_led(ledPins[6])
        elif (voltage > 1.90):
            alertor(2500)
            switch_led(ledPins[5])
        elif (voltage > 1.50):
            alertor(3000)
            switch_led(ledPins[4])
        elif (voltage > 1.20):
            alertor(3500)
            switch_led(ledPins[3])
        elif (voltage > 0.90):
            alertor(4000)
            switch_led(ledPins[2])
        elif (voltage > 0.45):
            alertor(4500)
            switch_led(ledPins[1])
        elif (voltage > 0.15):
            alertor(5000)
            switch_led(ledPins[0])
      
        


def destroy():
    bus.close()
    for pin in ledPins:
        GPIO.output(pin, GPIO.HIGH) # Set all ledPins to high(+3.3V) to off led
    GPIO.cleanup()

def alertor(tone):
    p.start(50)
    for x in range(0,361): #frequency of the alarm along the sine wave change
        sinVal = math.sin(x * (math.pi / 180.0)) #calculate the sine value
        toneVal = 10000 - (tone*2) + (sinVal * 500) #Add to the resonant frequency with a Weighted
        #print ('Sinval is %.2f tone is %d'%(sinVal, toneVal))
        if (toneVal > 2000):
            p.ChangeFrequency(toneVal) #output PWM
        time.sleep(0.001)

def setup():
    global p
    print ('Program is starting...')
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    GPIO.setup(buzzerPin, GPIO.OUT) # Buzzer Pin
    p = GPIO.PWM(buzzerPin, 1)
    p.start(0);

    for pin in ledPins:
        GPIO.setup(pin, GPIO.OUT)   # Set all ledPins' mode is output
        GPIO.output(pin, GPIO.HIGH) # Set all ledPins to high(+3.3V) to off led
        
if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()
