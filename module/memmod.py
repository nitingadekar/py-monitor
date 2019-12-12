#!/usr/bin/python
import psutil
def mem():
    mem=psutil.virtual_memory() [2]
   # print mem
    return mem;





#THRESHOLD = 90
#    if mem.available >= THRESHOLD:
#        print("warning")
#    else 
#        print ("current memory", psutil.virtual_memory() [2])


#mem()


