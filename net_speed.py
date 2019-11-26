#!/usr/bin/python3
def find_path():
    import glob
    for path in glob.glob("/sys/class/net/e*/speed"):
        #print(path)
        return path;
def get_speed():
    eth_path=find_path()
    #print (eth_path)
    value = []
    with open(eth_path,'r') as foo:
        for line in foo:
            value.append(line.split(None,1)[0])
            speed=value[0]
            #print (speed)
            return speed;

