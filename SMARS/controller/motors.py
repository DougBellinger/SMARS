import RPi.GPIO as GPIO  # @UnresolvedImport

class Motors:
    # Pin definitions - EN pins are PWM0, PMW1
    motor_1en = 12 
    motor_1a = 23 
    motor_1b = 24 
    motor_2en = 13 
    motor_2a = 27 
    motor_2b = 17 
    def __init__(self, e1=12,a1=24,b1=23,e2=13,a2=17,b2=27):
        global motor_1en, motor_1a, motor_1b, motor_2en, motor_2a, motor_2b
        motor_1en = e1 
        motor_1a = a1 
        motor_1b = b1 
        motor_2en = e2 
        motor_2a = a2 
        motor_2b = b2 
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