#-----------------------------------------------------------
# The following code connects to a device

def connect(dev_ip,username,password):

    print '--- attempting to: ssh '+username+'@'+dev_ip

    session = pexpect.spawn('ssh '+username+'@'+dev_ip, timeout=20)
    result = session.expect(['password:', pexpect.TIMEOUT])

    # Check for failure
    if result != 0:
        print '--- Timout or unexpected reply from device'
        return 0

    print '--- attempting to: password: '+password

    # Successfully got password prompt, logging in with password
    session.sendline(password)
    session.expect('#')

    return session  # return pexpect session object to caller

#-----------------------------------------------------------
#Call above function:
session = connect('10.0.0.1','cisco','cisco')

#---- Function to read device information from file -------------------
def read_device_info():

    # Read in the devices from the file
    file = open('devices','r')
    for line in file:

        device_info_list = line.strip().split(',') # Get device info into list
        devices_list.append(device_info_list)

    file.close() # Close the file since we are done with it

#---- Function to go through devices printing them to table -----------
def print_device_info():

    print ''
    print 'Name     OS-type  IP address           Software         '
    print '------   -------  ------------------   ------------------'

    # Go through the list of devices, printing out values in nice format
    for device in devices_list:

        print '{0:8} {1:8} {2:20} {3:20}'.format(device[0],device[1],
                                                 device[2],device[3])

    print ''
	
#---- Main: read device info, then print ------------------------------

devices_list = [] # Create the outer list for all devices

read_device_info()
print_device_info()

#---- Function to read device information from file -------------------
def read_device_info(devices_file):

    # Read in the devices from the file
    file = open(devices_file,'r')
    for line in file:

        device_info_list = line.strip().split(',') # Get device info into list
        devices_list.append(device_info_list)

    file.close() # Close the file since we are done with it
	

#---- Function to go through devices printing them to table -----------
def print_device_info(list_of_devices):

    print ''
    print 'Name     OS-type  IP address           Software         '
    print '------   -------  ------------------   ------------------'

    # Go through the list of devices, printing out values in nice format
    for device in list_of_devices:

        print '{0:8} {1:8} {2:20} {3:20}'.format(device[0],device[1],
                                                 device[2],device[3])

    print ''
	

#---- Main: read device info, then print ------------------------------

devices_list = [] # Create empty list of devices

print ''
devices_file = raw_input('Enter devices filename:')


read_device_info(devices_file)
print_device_info(devices_list)


