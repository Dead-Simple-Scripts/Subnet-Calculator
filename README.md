# Subnet-Calculator
Python script to calculate subnet information.

usage: subnet_calc.py [-h] --host HOST -m MASK

Usage: python subnet.py --host 10.0.0.0 -m 16 > subnet.txt

Generating a host list is an interactive CLI question|option.

OUTPUT Example:

$ python3 subnet_calc.py --host 10.0.0.0 -m 20

Do you want a list of all the hosts in the subnet? [y | n]


[*] Network (long):     10.0.0.0/255.255.240.0

[*] Network (short):    10.0.0.0/20

[*] Broadcast:          10.0.15.255

[*] Host Mask:          0.0.15.255

[*] Net Mask:           255.255.240.0

[*] Minimun Host:       10.0.0.1

[*] Maximum Host:       10.0.15.254

[*] Hosts per Network:  4094


#############

  Host List
  
#############  

10.0.0.1

10.0.0.2

10.0.0.3

10.0.0.4

10.0.0.5

10.0.0.6

10.0.0.7
