import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN = 24
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(PIN)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)


