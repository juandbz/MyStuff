#!/usr/bin/env python
import getpass
import sys
import telnetlib

user = raw_input("Enter your remote name account: ")
password = getpass.getpass()

for n in range (150,155):
    HOST = ("192.168.1." + str(n) +"\n")

    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("conf t\n")

    for n in range (2,11):
         tn.write("vlan " + str(n) +"\n")
         tn.write("name python_vlan_" + str(n) +"\n")
    tn.write("end\n")
    tn.write("wr\n")
    tn.write("exit\n")

    print tn.read_all()