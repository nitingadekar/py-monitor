#!/usr/bin/env python
import psutil
# gives a single float value
cpu=psutil.cpu_percent()
# gives an object with many fields
mem=psutil.virtual_memory()
# you can convert that object to a dictionary 
function=dict(psutil.virtual_memory()._asdict())

print (cpu)
print ("memory utilization", mem)

