#!/usr/bin/env python

from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException


print('''

----------------------Disclaimer-----------------------------

 Hello Users, I have created this script for configuration of
 multiple Cisco devices. Feel free to modify it but dont
 use this script for malisious activity & use it on your own risk
 I have tested this script against various types of Cisco Routers
 & Switches so if you observed any issue, then feel free to
 contact me.

-------------------------------------------------------------

Author      :- Preetam Patankar
Email-ID    :- web.preetam@gmail.com

-------------------------------------------------------------

''')


# Accepting Credentials for login
username = input('Enter your SSH username:- ')
password = getpass()


# Reading commands from .txt file
with open('config_cmd.txt') as f:
    commands_to_send = f.read().splitlines()

# Reading IP Address List from .txt file
with open('device_list.txt') as d:
    devices_list = d.read().splitlines()



for devices in devices_list:
    print('\n\n\n------------------------------------------')
    print ('Connecting to device - ' + devices)
    print('------------------------------------------')
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password
        }

# Trying to login into device
    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print('Authentication Failure, please confirm your credentials for device -> ', ip_address_of_device)
        continue
    except (NetMikoTimeoutException):
        print('Timeout Issue, Device taking longer time for login -> ', ip_address_of_device)
        continue
    except (EOFError):
        print('End of IP list file while trying to connect -> ', ip_address_of_device)
        continue
    except (SSHException):
        print('SSH Issue, please check SSH is configured correctly or not on this device -> ', ip_address_of_device)
        continue
    except Exception as unknown_error:
        print('There is some unusual error while login into this device -> ', ip_address_of_device)
        continue

# Sending commands to device
    output = net_connect.send_config_set(commands_to_send)
    print(output)
    print('------------------------------------------')
    
