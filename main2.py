# coding:utf-8
import temperature as temper
import operatePod as opPod
import time as time
import datetime as datetime
import sys as sys                                                                                                                                                 

#running_time :稼働時間(秒)　#check_interval :温度計測間隔(秒)　#max_temperature:設定温度()
def main(max_temperature):
                                                                                                                                                                              #ログファイル
    pod = opPod.OperatePod()

    start = time.time()
    elapse = 0

    temperature = 0
    #max 120 min
    while temperature < max_temperature:

        temperature = temper.getTemperature()

	print(temperature,max_temperature)

        if temperature <= max_temperature :
            print("turn on")
            pod.turn_on()
        elif temperature >= max_temperature:
            print("turn off")
            pod.turn_off()
	    break
        time.sleep(30)
        elapse = time.time()

    pod.turn_off()
    pod.end()

    #log.close()
    print("設定温度に到達しました")

main( int(sys.argv[1]) )
