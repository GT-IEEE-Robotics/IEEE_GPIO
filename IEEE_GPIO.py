
#import Adafruit_BBIO.GPIO as GPIO
import sys
sys.path.append('BeagleBone/adafruit-beaglebone-io-python-master')
import Adafruit_BBIO.GPIO as BGPIO
sys.path.append('Jetson/jetson-gpio-master/lib/python')
import Jetson.GPIO as JGPIO
import Adafruit_BBIO.PWM as PWM
import time


import sys
sys.path.append('Jetson/jetson-gpio-master/lib/python')
sys.path.append('Jetson/jetson-gpio-master/lib/python/Jetson/GPIO')
import Jetson.GPIO as JGPIO
import Adafruit_BBIO.PWM as PWM

class IEEE_GPIO:

    def __init__(self, platform):
        if platform != "Jetson" or platform != "BeagleBone" or platform != "RaspberryPi":
            raise Exception("Platform isn't compatible. Requires Jetson, BeagleBone, or RaspberryPi.")
        self.platform = platform

    def set_pin_input(input_pin):
        if self.platform == "Jetson" or self.platform == "RaspberryPi":
            JGPIO.setmode(JGPIO.BOARD)  #BCM pin-numbering scheme for 40 pins

            prev_value = None

            # Pin Setup:
            JGPIO.setup(input_pin, JGPIO.IN)  # set pin as an input pin
            try:
                while True:
                    value = JGPIO.input(input_pin)
                    if value != prev_value:
                        prev_value = value
                    time.sleep(1)
            finally:
                JGPIO.cleanup()
        else:
            BGPIO.setup("P8_7", OUT)

    def set_pin_output(output_pin):
        if self.platform == "Jetson" or self.platform == "RaspberryPi":
            # Pin Setup:
            JGPIO.setmode(JGPIO.BOARD)
            # set pin as an output pin with optional initial state of HIGH
            JGPIO.setup(output_pin, JGPIO.OUT, initial=JGPIO.HIGH)

            curr_value = JGPIO.HIGH
            try:
                while True:
                    time.sleep(1)
                    # Toggle the output every second
                    print("Outputting {} to pin {}".format(curr_value, output_pin))
                    JGPIO.output(output_pin, curr_value)
                    curr_value ^= JGPIO.HIGH
            finally:
                JGPIO.cleanup()

        else:
            BGPIO.setup("P8_7", IN)

    def set_pin_pwn(output_pin):
        if self.platform == "Jetson" or self.platform == "RaspberryPi":
            # Pin Setup:
            JGPIO.setmode(JGPIO.BOARD)
            # set pin as an output pin with optional initial state of HIGH
            JGPIO.setup(output_pin, JGPIO.OUT, initial=JGPIO.HIGH)
            p = JGPIO.PWM(output_pin, 50)
            p.start(25)

            try:
                while True:
                    time.sleep(1)
            finally:
                p.stop()
                JGPIO.cleanup()
        else:
            PWM.start("P9_14", 50, 2000, 1)
            PWM.cleanup()
            PWM.start("P9_14", 50, 2000, 0)
            PWM.cleanup()
