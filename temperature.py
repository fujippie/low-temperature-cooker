from w1thermsensor import W1ThermSensor

def getTemperature():

    sensor = W1ThermSensor()
    temperature_in_celsius = sensor.get_temperature()
    return temperature_in_celsius

def test():
    print(getTemperature)

'''
temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
temperature_in_all_units = sensor.get_temperatures([
    W1ThermSensor.DEGREES_C,
    W1ThermSensor.DEGREES_F,
    W1ThermSensor.KELVIN])
'''