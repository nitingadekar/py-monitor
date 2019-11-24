#!/usr/bin/python
#import psutil
import cpumod
import memmod
import diskmod 
cpupercent = cpumod.cpu()
cputhresh = 70
if cpupercent >= cputhresh: 
    print("CPU Utilisation is critical at {}% crossed  threshold {}%".format(cpupercent,cputhresh)) 
else :
    print("CPU utilization is normal at {}% and havent crossed warning threshold {}%".format(cpupercent,cputhresh))
#cpumod.cpu()
mempercent = memmod.mem()
memthresh = 80
if mempercent >= memthresh:
    print ("Memory Utilisation is critical at {}% crossed threshold {}%".format(mempercent,memthresh))
else: 
    print ("Memory utilization is normal at {}% and havent crossed warning threshold {}%".format(mempercent,memthresh))

#diskmod()
diskpercent = diskmod.disk_root()
diskthresh = 90

if diskpercent >= diskthresh:
    print ("Root storage is critical at {}% crossing  alert threshold {}%".format (diskpercent,diskthresh))
else:
    print ("Root storage utilized {}% below threshold {}% ".format (diskpercent,diskthresh))
