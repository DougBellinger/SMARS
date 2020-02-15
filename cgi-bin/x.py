import time
import RPi.GPIO as GPIO

# Pin definitions
motor_pwm = 12 # map to GP12 on SparkFun H-Bridge
motor_1 = 23 # map to GP47
motor_2 = 24 # map to GP48
motor_stby = 25 # map to GP49

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(motor_pwm, GPIO.OUT)
GPIO.setup(motor_1, GPIO.OUT)
GPIO.setup(motor_2, GPIO.OUT)
GPIO.setup(motor_stby, GPIO.OUT)

GPIO.output(motor_1, True)
GPIO.output(motor_2, False)
GPIO.output(motor_stby, False)

#1000 Hz, 90% duty cycle
print "starting motor"
pwm = GPIO.PWM(motor_pwm, 100)
pwm.start(100)
time.sleep(2)
pwm.ChangeDutyCycle(50)
time.sleep(2)

# Stop, cleanup, and exit
pwm.stop()
GPIO.cleanup()
