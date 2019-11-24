#!/usr/bin/python
import psutil

def get_network():
    network = psutil.net_io_counters(pernic=True)
    ifaces = psutil.net_if_addrs()
    networks = list()
    for k, v in ifaces.items():
        ip = v[0].address
        data = network[k]
        ifnet = dict()
        ifnet['ip'] = ip
        ifnet['iface'] = k
        ifnet['sent'] = '%.2fMB' % (data.bytes_sent/1024/1024)
        ifnet['recv'] = '%.2fMB' % (data.bytes_recv/1024/1024)
        ifnet['packets_sent'] = data.packets_sent
        ifnet['packets_recv'] = data.packets_recv
        ifnet['errin'] = data.errin
        ifnet['errout'] = data.errout
        ifnet['dropin'] = data.dropin
        ifnet['dropout'] = data.dropout
        networks.append(ifnet)
    return networks 

get_network()
print get_network() 
