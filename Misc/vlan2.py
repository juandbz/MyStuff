#!/usr/bin/env python
import getpass
import sys
import telnetlib

HOST = "192.168.1.150"
user = raw_input("Enter your remote name account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")



tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("exit\n")
tn.write("vlan 3\n")
tn.write("exit\n")
tn.write("vlan 4\n")
tn.write("exit\n")
tn.write("vlan 5\n")
tn.write("exit\n")


print tn.read_all()