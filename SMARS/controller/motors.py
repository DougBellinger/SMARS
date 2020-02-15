# Pin definitions
import time 
import RPi.GPIO as GPIO  # @UnresolvedImport
#import sys
#sys.path.append(r'/usr/lib/cgi-bin')
#import pydevd  # @UnresolvedImport
#pydevd.settrace('192.168.2.63') # replace IP with address
                                # of Eclipse host machine

class Motors:
    motor_1en = 25 
    motor_1a = 23 
    motor_1b = 24 
    motor_2en = 22 
    motor_2a = 27 
    motor_2b = 17 
    def __init__(self, e1=25,a1=23,b1=24,e2=22,a2=27,b2=17):
        global motor_1en, motor_1a, motor_1b, motor_2en, motor_2a, motor_2b
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
    
    def left(self, n):
        self.motors(n, 0b01, 0b01)
    
    def right(self, n) :
        self.motors(n, 0b10, 0b10)
    
    def rev(self, n): 
        self.motors(n, 0b01, 0b01)
    
    def fwd(self, n) :
        return(self.motors(n, 0b10, 0b10))
    
    def stop(self):
        self.motors(0, 0b00, 0b00)
    
    
    def motors(self, n, m1, m2) :
        GPIO.output(motor_1a, m1 & 0b01);
        GPIO.output(motor_1b, m1 & 0b10);
        GPIO.output(motor_2a, m2 & 0b01);
        GPIO.output(motor_2b, m2 & 0b10);
        GPIO.output(motor_1en, True);
        GPIO.output(motor_2en, True);
        if (n > 0) :
            return(n*100)
               
    
    def end(self) :
        GPIO.cleanup();