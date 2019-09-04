# coding:utf-8
import temperature as temper
import operatePod as opPod
import time as time
import datetime as datetime

#running_time :稼働時間(秒)　#check_interval :温度計測間隔(秒)　#max_temperature:設定温度(℃)
def main(running_time,check_interval,max_temperature):
    #ログファイル
    log = open(  "log/"+datetime.datetime.now().strftime("%m-%d_%H-%M")  +".txt",'w')
    log.write("start稼働，間隔，設定温度="+ str(running_time) +","+ str(check_interval )+","+ str(max_temperature) +"\n")

    pod = opPod.OperatePod()

    start = time.time()
    elapse = 0

    while elapse - start <= running_time:
        temperature = temper.getTemperature()
        log.write("時間"+ datetime.datetime.now().strftime("%H-%M-%S") +"/温度:" + str( temperature ) +"℃\n")
        if temperature <= max_temperature :
            pod.turn_on()
        elif temperature >= max_temperature:
            pod.turn_off()
        time.sleep(check_interval) 
        elapse = time.time()

        print("temperature",temperature,"elapse-start",elapse - start)

    pod.end()
    log.close()

main(33*60,3,69)

