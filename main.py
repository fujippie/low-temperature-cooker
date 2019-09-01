# coding:utf-8
import temperature as temper
import operatePod as opPod
import time as time

#main
#running_time   :稼働時間(秒)
#check_interval :温度計測間隔(秒)
#max_temperature:設定温度(℃)
def main(running_time,check_interval,max_temperature):
    pod = opPod.OperatePod()

    start = time.time()
    elapse = 0

    while elapse - start == running_time:
        temperature = temper.getTemperature()
        if temperature <= max_temperature :
            pod.turn_on()
        elif temperature >= max_temperature:
            pod.turn_off()
        time.sleep(check_interval) #20秒ごとに温度を測定
        elapse = time.time()

    pod.end()

    print("")


main(10,5,60)

