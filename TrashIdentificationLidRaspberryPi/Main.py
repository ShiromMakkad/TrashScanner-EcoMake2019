import os
import sys
import ArduinoInterface
import time
import _thread
import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        _thread.start_new_thread( ArduinoInterface.Arduino().begin, () )
    except:
        print("Error: unable to start thread")

def loop():
    state = 0

    while (True):
        statement = "Light: " + str(ArduinoInterface.Sensors.Light.light)

        if (GPIO.input(23) == False):
            #Left
            ArduinoInterface.Outputs.Motors.motor1 = 25;
            ArduinoInterface.Outputs.Motors.motor2 = -25;
        elif(GPIO.input(24) == False):
            #Center
            ArduinoInterface.Outputs.Motors.motor1 = 3;
            ArduinoInterface.Outputs.Motors.motor2 = 3;
        elif(GPIO.input(26) == False):
            #Right
            ArduinoInterface.Outputs.Motors.motor1 = -25;
            ArduinoInterface.Outputs.Motors.motor2 = 25;

        time.sleep(0.05)

def main():
    setup()

    while(ArduinoInterface.Arduino.ready == False):
        time.sleep(0.1)

    time.sleep(1) #The first few sensor readings are usually bogus

    loop()

if __name__ == "__main__":
    main()