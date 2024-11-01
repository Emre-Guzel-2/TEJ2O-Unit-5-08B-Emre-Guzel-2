"""
Created by: Emre Guzel
Created on: Oct 31 2024
This module is a Micro:bit MicroPython program  tuns 2 motors and stops them when the distacne is smaler tahn 10 cm
"""
#test
from microbit import *
import RPi.GPIO as GPIO
from stepper import StepperMotor





class HCSR04:
    # this class abstracts out the functionality of the HC-SR04 and
    #   returns distance in mm
    # Trig: pin 1
    # Echo: pin 2
    def __init__(self, tpin=pin1, epin=pin2, spin=pin13):
        self.trigger_pin = tpin
        self.echo_pin = epin
        self.sclk_pin = spin

    def distance_mm(self):
        spi.init(baudrate=125000, sclk=self.sclk_pin,
                 mosi=self.trigger_pin, miso=self.echo_pin)
        pre = 0
        post = 0
        k = -1
        length = 500
        resp = bytearray(length)
        resp[0] = 0xFF
        spi.write_readinto(resp, resp)
        # find first non zero value
        try:
            i, value = next((ind, v) for ind, v in enumerate(resp) if v)
        except StopIteration:
            i = -1
        if i > 0:
            pre = bin(value).count("1")
            # find first non full high value afterwards
            try:
                k, value = next((ind, v)
                                for ind, v in enumerate(resp[i:length - 2]) if resp[i + ind + 1] == 0)
                post = bin(value).count("1") if k else 0
                k = k + i
            except StopIteration:
                i = -1
        dist= -1 if i < 0 else round(((pre + (k - i) * 8. + post) * 8 * 0.172) / 2)
        return dist
    
class StepperMotor:
    def __init__(self, pins):
        self.pins = pins
        GPIO.setmode(GPIO.BCM)
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
        
        # Define the 8-step sequence for the motor
        self.sequence = [
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]
        ]
    
    def step(self, steps, delay=0.001):
        for _ in range(steps):
            for step in self.sequence:
                for pin in range(4):
                    GPIO.output(self.pins[pin], step[pin])
                time.sleep(delay)
    
    def cleanup(self):
        GPIO.cleanup()



# Setting the varribels 
distacneToObject  = 0
sonar = HCSR04
pins = [17, 18, 27, 22]  
motor = StepperMotor(pins)


# Setting the screen
display.clear()
display.show(Image.HAPPY)

# When it is clikes a it will going to mesuare the distacne and make the mootrs work 
while True: 
    if button_a.is_pressed():
        display.clear()
        
        