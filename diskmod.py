#!/usr/bin/python

def disk_root():
    import psutil
    diskroot=psutil.disk_usage('/') [3]
    #print (diskroot)
    return diskroot;

#disk_root()

