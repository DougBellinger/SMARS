import time
import RPi.GPIO as GPIO

# Pin definitions
motor_pwm = 26 # map to GP12 on SparkFun H-Bridge
motor_1 = 4 # map to GP47
motor_2 = 5 # map to GP48
motor_stby = 6 # map to GP49

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(motor_pwm, GPIO.OUT)
GPIO.setup(motor_1, GPIO.OUT)
GPIO.setup(motor_2, GPIO.OUT)
GPIO.setup(motor_stby, GPIO.OUT)

GPIO.output(motor_1, True)
GPIO.output(motor_2, False)
GPIO.output(motor_stby, True)

# Initialize pwm object with 50 Hz and 0% duty cycle
pwm = GPIO.PWM(motor_pwm, 50)
pwm.start(0)

# Set PWM duty cycle to 50%, wait, then to 90%
pwm.ChangeDutyCycle(50)
time.sleep(2)
pwm.ChangeDutyCycle(90)
time.sleep(2)

# Stop, cleanup, and exit
pwm.stop()
GPIO.cleanup()
