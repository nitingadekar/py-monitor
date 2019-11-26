#!/usr/bin/python
import time 
import net_speed
import logging 
import os  
import cpumod
import memmod
import diskmod 
import msg_webhook
#get timestamp 
t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print (current_time)

#initialize log file
if not os.path.exists('./pymonit.log'):
    os.mknod('./pymonit.log')
if not os.path.exists('pymonit-warn.log'):
    os.mknod('./pymonit-warn.log')
#log= open("./cpu.log".a)
#log.close()

logging.basicConfig(filename="pymonit.log", level=logging.INFO)
#logging.basicConfig(filename="pymonit-warn.log", level=logging.WARN)

#monitor CPU utilization
cpupercent = cpumod.cpu()
cputhresh = 80
if cpupercent >= cputhresh: 
    print("CPU Utilisation is critical at {}% crossed  threshold {}%".format(cpupercent,cputhresh)) 
    #send alert to slack #monitoring channel
    msg_webhook.slack_msg("CPU Utilisation is critical at {}% crossed  threshold {}%".format(cpupercent,cputhresh))
    logging.warn("{} CPU Utilisation is critical at {}% crossed  threshold {}%".format(current_time,cpupercent,cputhresh))
else :
    print("CPU utilization is normal at {}% and havent crossed warning threshold {}%".format(cpupercent,cputhresh))
    #msg_webhook.slack_msg("CPU utilization is normal at {}% and havent crossed warning threshold {}%".format(cpupercent,cputhresh))
    logging.info("{} CPU utilization is {}% and havent crossed warning threshold {}%".format(current_time,cpupercent,cputhresh))
#cpumod.cpu()

#monitor memory utilization 
mempercent = memmod.mem()
memthresh = 80
if mempercent >= memthresh:
    print ("Memory Utilisation is critical at {}% crossed threshold {}%".format(mempercent,memthresh))
    #send alert to slack #monitoring channel
    msg_webhook.slack_msg("Memory Utilisation is critical at {}% crossed threshold {}%".format(mempercent,memthresh))
    logging.warn("{}Memory Utilisation is critical at {}% crossed threshold {}%".format(current_time,mempercent,memthresh))
else: 
    print ("Memory utilization is normal at {}% and havent crossed warning threshold {}%".format(mempercent,memthresh))
    #msg_webhook.slack_msg("Memory utilization is normal at {}% and havent crossed warning threshold {}%".format(mempercent,memthresh))
    logging.info("{} Memory utilization is {}% and haven't crossed warning threshold {}%".format(current_time,mempercent,memthresh))

#monitor root directory utilization

diskpercent = diskmod.disk_root()
diskthresh = 90

if diskpercent >= diskthresh:
    print ("Root storage is critical at {}% crossing  alert threshold {}%".format (diskpercent,diskthresh))
    #send alert to slack #monitoring channel
    msg_webhook.slack_msg("Root storage is critical at {}% crossing  alert threshold {}%".format (diskpercent,diskthresh))
    logging.warn("{} Root storage is critical at {}% crossing  alert threshold {}%".format (current_time,diskpercent,diskthresh))
else:
    print ("Root storage utilized {}% below threshold {}% ".format (diskpercent,diskthresh))
    #msg_webhook.slack_msg("Root storage utilized {}% below threshold {}% ".format (diskpercent,diskthresh))
    logging.info("{} Root storage utilized {}% below threshold {}%".format (current_time,diskpercent,diskthresh))
    



netspeed = net_speed.get_speed()
netthresh = 2
if netspeed <= netthresh:
    print ("Net speed is critical at {}Mbps less than threshold {}Mbps".format(netspeed,netthresh))
    msg_webhook.slack_msg("Ethernet speed is critical at {}% crossed threshold {}%".format(netpercent,netthresh))
    logging.warn("{} Ethernet speed is critical at {}Mbps crossed threshold {}Mbps".format(current_time,netspeed,netthresh))
else:
    print("Net speed is {}Mbps not yet crossed threshold of {}Mbps".format(netspeed,netthresh))
    #msg_webhook.slack_msg("Net speed is {}Mbps not yet crossed threshold of {}Mbps".format(netspeed,netthresh))
    logging.info("{} Net speed is {}Mbps not yet crossed threshold of {}Mbps".format(current_time,netspeed,netthresh))

