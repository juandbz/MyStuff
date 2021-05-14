#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.72',
    'username': 'juan',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.73',
    'username': 'juan',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.74',
    'username': 'juan',
    'password': 'cisco',
}

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
        print ('Creating VLAN ' + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_Vlan ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print (output)


config_commands = ['int loop0 ', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)