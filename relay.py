import RPi.GPIO as GPIO
import time
from threading import Timer

gpio6 = 6 # relay gate0
gpio20 = 20 # relay gate1
gpio26 = 26 # remote control gate0
gpio16 = 16 # remote control gate1
gpio05 = 5 # sensor of gate0
gpio19 = 19 # sensor of gate1
gate_counter = 0

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio26, GPIO.IN)
GPIO.setup(gpio16, GPIO.IN)
GPIO.setup(gpio05, GPIO.IN)
GPIO.setup(gpio19, GPIO.IN)
GPIO.setup(gpio6, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(gpio20, GPIO.OUT, initial=GPIO.LOW)

def motor_on(pin):
    print('motor_on', pin)
    GPIO.output(pin, GPIO.HIGH) # Turn motor on

def motor_off(pin):
    print('motor_off', pin)
    GPIO.output(pin, GPIO.LOW) # Turn motor off

def gate0(test):
    if GPIO.input(gpio05):
        return
    motor_on(gpio6)
    r = Timer(1.0, motor_off, (gpio6,)) 
    r.start()

def gate1(test):
    if GPIO.input(gpio19):
        return
    motor_on(gpio20)
    r = Timer(1.0, motor_off, (gpio20,))
    r.start()

GPIO.add_event_detect(gpio26, GPIO.RISING, callback=gate0, bouncetime=1300)
GPIO.add_event_detect(gpio16, GPIO.RISING, callback=gate1, bouncetime=1300)

if __name__ == '__main__':
    print('System ready!')
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()

# if __name__ == '__main__':
#     try:
#         # motor_on(gpio6)
#         # motor_on(gpio20)
#         time.sleep(1)
#         # motor_off(gpio6)
#         # motor_off(gpio20)
#         time.sleep(1)
#         GPIO.cleanup()
#     except KeyboardInterrupt:
#         GPIO.cleanup()
