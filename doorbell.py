import RPi.GPIO as GPIO

buzzerPin = 11    # define the buzzerPin
buttonPin = 12    # define the buttonPin 9306158436


def setup():
	#print ('Program is starting...')
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(buzzerPin, GPIO.OUT)   # Set buzzerPin's mode is output
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set buttonPin's mode is input, and pull up to high level(3.3V)

def loop():
	while True:
		if GPIO.input(buttonPin)==GPIO.HIGH:
			GPIO.output(buzzerPin,GPIO.HIGH)
			print ('buzzer on ...')
		else :
			GPIO.output(buzzerPin,GPIO.LOW)
			print ('buzzer off ...')

def destroy():
	GPIO.output(buzzerPin, GPIO.LOW)     # buzzer off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
