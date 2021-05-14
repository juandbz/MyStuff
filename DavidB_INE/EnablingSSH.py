import getpass
import telnetlib

user = input('Enter your telnet username: ')
password = getpass.getpass()

f = open('myswitches')

for IP in f:
    IP = IP.strip()
    print ('Enabling SSH on switch ' + (IP))
    HOST=IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    tn.write(b'conf t\n')
    tn.write(b'username juan password cisco\n')
    tn.write(b'username juan priv 15\n')
    tn.write(b'line vty 0 4\n')
    tn.write(b'login local\n')
    tn.write(b'transport input all\n')
    tn.write(b'exit\n')
    tn.write(b'ip domain-name madeuppp123.com\n')
    tn.write(b'crypto key generate rsa\n')
    tn.write(b'1024\n')
    tn.write(b'end\n')
    tn.write(b'exit\n')

    print(tn.read_all().decode('ascii'))
