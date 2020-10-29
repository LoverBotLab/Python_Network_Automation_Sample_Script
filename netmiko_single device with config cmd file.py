#!/usr/bin/env python

from netmiko import ConnectHandler

with open('show_cmd.txt') as f:
    commands_to_send = f.read().splitlines()

with open('device_list.txt') as d:
    devices_list = d.read().splitlines()

for devices in devices_list:
    print 'Connecting to device" '+ devices
    ip_address_of+device = devices
    ios_devices = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'cisco',
        'password': 'cisco'
        }

all_devices = [ios_devices]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(commands_to_send)
    print(output)

