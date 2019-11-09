
#import Adafruit_BBIO.GPIO as GPIO
import sys
sys.path.append('Jetson/jetson-gpio-master/lib/python')
sys.path.append('Jetson/jetson-gpio-master/lib/python/Jetson/GPIO')
import Jetson.GPIO as JGPIO


class IEEE_GPIO:

    def __init__(self, platform):
        if platform != "Jetson" or platform != "BeagleBone" or platform != "RaspberryPi":
            raise Exception("Platform isn't compatible. Requires Jetson, BeagleBone, or RaspberryPi.")
        self.platform = platform

    def set_input_pin(input_pin):
        JGPIOGPIO.setmode(JGPIO.BOARD)  #BCM pin-numbering scheme for 40 pins

        prev_value = None

        # Pin Setup:
        JGPIO.setup(input_pin, JGPIO.IN)  # set pin as an input pin
        try:
            while True:
                value = JGPIO.input(input_pin)
                if value != prev_value:
                    if value == JGPIO.HIGH:
                        value_str = "HIGH"
                    else:
                        value_str = "LOW"
                    print("Value read from pin {} : {}".format(input_pin,
                                                               value_str))
                    prev_value = value
                time.sleep(1)
        finally:
            JGPIO.cleanup()

    def set_pin_output(output_pin):
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

    def set_pin_pwn(output_pin):
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
