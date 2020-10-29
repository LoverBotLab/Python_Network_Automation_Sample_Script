#!/usr/bin/env python

from netmiko import ConnectHandler

ios_RTR = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.201",
    "username": "cisco",
    "password": "cisco"
}

net_connect = ConnectHandler(**ios_RTR)
output = net_connect.send_command('show ip int brief')
print(output)
