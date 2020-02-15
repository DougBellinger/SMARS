# Pin definitions
import time
import RPi.GPIO as GPIO
import sys
sys.path.append(r'/usr/lib/cgi-bin')
import pydevd
pydevd.settrace('192.168.2.63') # replace IP with address
                                # of Eclipse host machine

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

def left(n): 
	motors(n, 0b01, 0b01)

def right(n) :
	motors(n, 0b10, 0b10)

def rev(n): 
	motors(n, 0b01, 0b01)

def fwd(n) :
	motors(n, 0b10, 0b10)

def stop():
	motors(0, 0b00, 0b00)


def motors(n, m1, m2) :
	GPIO.output(motor_1a, m1 & 0b01);
	GPIO.output(motor_1b, m1 & 0b10);
	GPIO.output(motor_2a, m2 & 0b01);
	GPIO.output(motor_2b, m2 & 0b10);
	GPIO.output(motor_1en, True);
	GPIO.output(motor_2en, True);
	if (n > 0) :
		time.sleep(n)
		GPIO.output(motor_1en, False)
		GPIO.output(motor_2en, False)

def end() :
	GPIO.cleanup();
