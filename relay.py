import RPi.GPIO as GPIO
import time
from threading import Timer, Lock
from datetime import datetime

gpio23 = 23 # relay gate0
gpio17 = 17 # relay gate1
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
GPIO.setup(gpio23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(gpio17, GPIO.OUT, initial=GPIO.LOW)

lock = Lock()

def motor_on(pin):
    print('motor_on', pin)
    GPIO.output(pin, GPIO.HIGH) # Turn motor on

def motor_off(pin):
    print('motor_off', pin)
    GPIO.output(pin, GPIO.LOW) # Turn motor off

def gate0(test):
    lock.acquire()
    colision_gate1 = GPIO.input(gpio16)
    if GPIO.input(gpio05) or colision_gate1 or GPIO.input(gpio17):
        lock.release()
        if colision_gate1:
            print('Gate0 reports colision with gate1 ', datetime.now())
        return
    motor_on(gpio23)
    r = Timer(1.0, motor_off, (gpio23,))
    r.start()
    lock.release()

def gate1(test):
    lock.acquire()
    colision_gate0 = GPIO.input(gpio26)
    if GPIO.input(gpio19) or colision_gate0 or GPIO.input(gpio23):
        lock.release()
        if colision_gate0:
            print('Gate1 reports colision with gate0 ', datetime.now())
        return
    motor_on(gpio17)
    r = Timer(1.0, motor_off, (gpio17,))
    r.start()
    lock.release()

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
#         # motor_on(gpio23)
#         # motor_on(gpio17)
#         time.sleep(1)
#         # motor_off(gpio23)
#         # motor_off(gpio17)
#         time.sleep(1)
#         GPIO.cleanup()
#     except KeyboardInterrupt:
#         GPIO.cleanup()
