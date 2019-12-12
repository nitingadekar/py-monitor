#!/usr/bin/python
import psutil
def cpu():
    cpupercent=psutil.cpu_percent(interval=1)
    #print cpupercent
    return cpupercent;


#cpu(1)


