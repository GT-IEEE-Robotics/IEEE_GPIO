import Jetson.GPIO as GPIO

class IEEE_GPIO:

    def __init__(self, platform):
        if (platform ! = "Jetson" or platform ! = "BeagleBone" or platform ! = "RaspberryPi") {
            raise Exception("Platform isn't compatible. Requires Jetson, BeagleBone, or RaspberryPi")
        }
        self.platform = platform

    def set_input_pin(input_pin):
        GPIO.setmode(GPIO.BOARD)  #BCM pin-numbering scheme for 40 pins

        prev_value = None

        # Pin Setup:
        GPIO.setup(input_pin, GPIO.IN)  # set pin as an input pin
        try:
            while True:
                value = GPIO.input(input_pin)
                if value != prev_value:
                    if value == GPIO.HIGH:
                        value_str = "HIGH"
                    else:
                        value_str = "LOW"
                    print("Value read from pin {} : {}".format(input_pin,
                                                               value_str))
                    prev_value = value
                time.sleep(1)
        finally:
            GPIO.cleanup()

    def set_pin_output(output_pin):
        # Pin Setup:
        GPIO.setmode(GPIO.BOARD)
        # set pin as an output pin with optional initial state of HIGH
        GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

        curr_value = GPIO.HIGH
        try:
            while True:
                time.sleep(1)
                # Toggle the output every second
                print("Outputting {} to pin {}".format(curr_value, output_pin))
                GPIO.output(output_pin, curr_value)
                curr_value ^= GPIO.HIGH
        finally:
            GPIO.cleanup()

    def set_pin_pwn(output_pin):
        # Pin Setup:
        GPIO.setmode(GPIO.BOARD)
        # set pin as an output pin with optional initial state of HIGH
        GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
        p = GPIO.PWM(output_pin, 50)
        p.start(25)

        try:
            while True:
                time.sleep(1)
        finally:
            p.stop()
            GPIO.cleanup()
