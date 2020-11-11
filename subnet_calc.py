# Script to calculate subnets.
# Usage: python subnet.py --host 10.0.0.0 -m 16 > subnet.txt
# Generating a host list is an interactive CLI question|option.

import argparse
from ipaddress import ip_interface

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="host address", required=True)
    parser.add_argument("-m", "--mask", help="mask", required=True)
    args = parser.parse_args()
    iface = ip_interface(f"{args.host}/{args.mask}")
    network = iface.network.network_address
    broadcast = iface.network.broadcast_address
    hostmask = iface.hostmask
    netmask = iface.netmask
    hosts = list(iface.network.hosts())
    minimum_host = min(hosts, default=None)
    maximum_hosts = max(hosts, default=None)

    #ask user if they want a host list
    print("Do you want a list of all the hosts in the subnet? [y | n]")
    printlist = input()

    print(
        f"""
[*] Network (long):     {network}/{netmask}
[*] Network (short):    {network}/{args.mask}
[*] Broadcast:          {broadcast}
[*] Host Mask:          {hostmask}
[*] Net Mask:           {netmask}
[*] Minimum Host:       {minimum_host}
[*] Maximum Host:       {maximum_hosts}
[*] Hosts per Network:  {len(hosts)}
""")
    #Prints a list of all the hosts
    if printlist == "y":
        print("""#############
  Host List
#############  """)
        for i in iface.network.hosts():
            print(i)
    else: pass

if __name__ == '__main__':
    main()
