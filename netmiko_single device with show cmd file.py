#!/usr/bin/env python

from netmiko import ConnectHandler

with open('show_cmd.txt') as f:
    commands_to_send = f.read().splitlines()

ios_devices = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.201',
    'username': 'cisco',
    'password': 'cisco'
    }

all_devices = [ios_devices]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for cmd in commands_to_send:
        output = net_connect.send_command(cmd)
        print(output)

