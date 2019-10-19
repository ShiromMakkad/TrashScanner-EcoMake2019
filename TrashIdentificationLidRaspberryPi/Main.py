import os
import sys
import ArduinoInterface
import time
import _thread

def setup():
    try:
        _thread.start_new_thread( ArduinoInterface.Arduino().begin, () )
    except:
        print("Error: unable to start thread")

def loop():
    while (True):
        statement = "Light: " + str(ArduinoInterface.Sensors.Light.light)
        print(statement, end = "\r")

        time.sleep(0.05)

def main():
    setup()

    while(ArduinoInterface.Arduino.ready == False):
        time.sleep(0.1)

    time.sleep(1) #The first few sensor readings are usually bogus

    loop()

if __name__ == "__main__":
    main()