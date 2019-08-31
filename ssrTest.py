
import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BOARD)

cooker_pin = 33
GPIO.setup(cooker_pin, GPIO.OUT)

def turn_on():
    GPIO.output(cooker_pin, True)
   # redis_db.set('cooker_is_heating', 'true')

def turn_off():
    GPIO.output(cooker_pin, False)
  #  redis_db.set('cooker_is_heating', 'false')
  
print("turn on")
turn_on()
print("sleep")
time.sleep(5)
print("turn off")
turn_off()
GPIO.cleanup()