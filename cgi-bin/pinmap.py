# Pin definitions
import RPi.GPIO as GPIO
import time
motor_1en = 25 
motor_1a = 23 
motor_1b = 24 
motor_2en = 22 
motor_2a = 27 
motor_2b = 17 
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_1en, GPIO.OUT)
GPIO.setup(motor_1a, GPIO.OUT)
GPIO.setup(motor_1b, GPIO.OUT)
GPIO.setup(motor_2en, GPIO.OUT)
GPIO.setup(motor_2a, GPIO.OUT)
GPIO.setup(motor_2b, GPIO.OUT)

def fwd(n) :
	GPIO.output(motor_1a, True);
	GPIO.output(motor_1b, False);
	GPIO.output(motor_2a, True);
	GPIO.output(motor_2b, False);
	GPIO.output(motor_2en, True);
	GPIO.output(motor_2en, True);
	if (n > 0) :
		time.sleep(n)
		GPIO.output(motor_1en, False)
		GPIO.output(motor_2en, False)
