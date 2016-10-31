import RPi.GPIO as GPIO
import time
import sys

# $./led.py 18
Usage = "led.py [PIN Number]"
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "\nBad amount of input arguments\n", Usage, "\n"
        sys.exit(1)

    try:
        PIN = int( sys.argv[1] )
    except:
        pass

    print( "PIN %i"%PIN )
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PIN,GPIO.OUT)
    print "LED on"
    GPIO.output(PIN,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(PIN,GPIO.LOW)

