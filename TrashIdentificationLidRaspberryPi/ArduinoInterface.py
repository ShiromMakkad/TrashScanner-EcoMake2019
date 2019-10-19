import serial
import time
import sys
import _thread

class Sensors:
    class Light:
        @property
        def light(self):
            return float(self._x)

        @light.setter
        def light(self, value):
            if 0 < value < 100000:
                self._x = value
            else:
                raise ValueError("Light must be between 0 and 1000")

class Arduino:
    ready = False

    def __init__(self):
        try:
            self.__ser = serial.Serial("COM3", baudrate = 115200)
        except:
            print("Unable to connect")

    def begin(self):
        transmissionStarted = False

        while(True):
            #Just for timing the loop
            startTime = time.time()

            arduinoData = self.__ser.readline()

            arduinoData = arduinoData.decode("utf-8")[:-2]
            #print(arduinoData)

            #Detects if the arduino is ready to transmit
            if(arduinoData == "A"):
                print("Starting Transmission!")
                transmissionStarted = True

                self._writeData()

                Arduino.ready = True;

                continue

            if(transmissionStarted):
                data = arduinoData.split(",")

                try:
                    Sensors.Light.light = float(data[0])
                except:
                    print("Data error                                                                               ", end="\r")

                self._writeData()

            endTime = time.time()

            #print(str((endTime - startTime) * 1000) + " ms")

    def _writeData(self):
        self.__ser.reset_input_buffer()

        writeString = ''.join([str(2), ","])

        self.__ser.write(writeString.encode("utf-8"))