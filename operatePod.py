
import RPi.GPIO as GPIO
import time as time

class OperatePod:
    cooker_pin =33
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.cooker_pin, GPIO.OUT)
    def end(self):
        self.turn_off()
        GPIO.cleanup()

    def turn_on(self):
        GPIO.output(self.cooker_pin, True)

    def turn_off(self):
        GPIO.output(self.cooker_pin, False)


obj = OperatePod()

print("turn on")
obj.turn_on()
print("sleep")
time.sleep(10)
print("turn off")
obj.turn_off()

obj.end()

