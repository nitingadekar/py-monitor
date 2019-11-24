#!/usr/bin/python
import psutil
stats = psutil.net_if_stats() 
io_counters = psutil.net_io_counters(pernic=True)
for nic, addrs in psutil.net_if_addrs().items():
    print("%s:" % (nic))
    if nic in stats:
        st = stats[nic]
        print("speed=%sMB, duplex=%s, mtu=%s, up=%s" % (
            st.speed, duplex_map[st.duplex], st.mtu,
            "yes" if st.isup else "no"))
 
