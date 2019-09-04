import time as time
import datetime as datetime

now = datetime.datetime.now()
a = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

print(now.strftime("%Y%m%d%H%M%S"))
log = open(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")+".txt",'w')
log.write("aaa\n")
log.write("asdsdsdaa\n")