
import temperature as temper
import operatePod as opPod

import time as time


print("hello::" , temper.getTemperature())

obj = opPod.OperatePod()

print("turn on")
obj.turn_on()
print("sleep")
time.sleep(10)
print("turn off")
obj.turn_off()

obj.end()
