# py-monitor
Simple monitoring tool for linux servers using python for CPU, Memory, Storage and Network
## Installation:
Install python3.5+ from [here](https://www.python.org/downloads/)
Install pip3 git and slack(optional)
Run below command to install dependencies
`pip3 install psutil slack requests logging glob`

Clone the repo by `git clone https://github.com/nitingadekar/py-monitor.git`

Run `python3 pymonit.py` to get the CPU, Memory, Root drive usage and Ethernet speed. 

For continuously monitoring the server add below cronjob for your frequency.
`*/5 * * * * /usr/bin/python3 /path/to/installed/pymonitor/pymonit.py`
A log file will be generated at same location with `pymonit.log` which will have logging of every execution.
 
