#################################
## CSV Module
## Readind CSV Files
#################################
 
###CSV File - (airtravel.csv) - attached to this lecture
# "Month", "1958", "1959", "1960"
# "JAN",  340,  360,  417
# "FEB",  318,  342,  391
# "MAR",  362,  406,  419
# "APR",  348,  396,  461
# "MAY",  363,  420,  472
# "JUN",  435,  472,  535
# "JUL",  491,  548,  622
# "AUG",  505,  559,  606
# "SEP",  404,  463,  508
# "OCT",  359,  407,  461
# "NOV",  310,  362,  390
# "DEC",  337,  405,  432
 
## Importing the module
import csv
 
## Opening the file in read-only mode. airtravel.csv is in the same directory with the python script
with open('airtravel.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)       # using a csv.reader object
 
    next(reader)    # skipping the first line (header)
    for row in reader:
       print(row)   # row is a list, each field is list element
 
 
#################################
## CSV Module
## Writing CSV Files
#################################
 
## Importing the module
import csv
 
## Opening people.csv in append-mode
with open('people.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)    # getting a csv.writer object
    csvdata = (5, 'Anne', 'Amsterdam')
    writer.writerow(csvdata)        # appending a line to the end file. csvdata is a tuple
 
 
## Opening numbers.csv in write-mode
with open('numbers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1, 101):
        writer.writerow([x, x**2, x**3, x**4])
 
 
#################################
## CSV Module
## Using CSV Dialects
#################################
 
import csv
 
## Printing available csv dialects
print(csv.list_dialects())
 
## passwd file - passwd.csv is attached to this lecture
# root:x:0:0:root:/root:/bin/bash
# daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
# bin:x:2:2:bin:/bin:/usr/sbin/nologin
# sys:x:3:3:sys:/dev:/usr/sbin/nologin
# sync:x:4:65534:sync:/bin:/bin/sync
# games:x:5:60:games:/usr/games:/usr/sbin/nologin
# man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
 
## Reading /etc/passwd (Linux file) using a custom delimiter (:)
with open('/etc/passwd', 'r') as f:
    reader = csv.reader(f, delimiter=':', lineterminator='\n')
    for row in reader:
        print(row)
 
 
## item.csv file (attached to this lecture)
# items#quantity#price
# pens#3#8.8
# plates#15#2.6
# cups#44#1.1
# bottles#21#3.5
 
## Creating a custom dialect named hashes
csv.register_dialect('hashes', delimiter='#', quoting=csv.QUOTE_NONE, lineterminator='\n')
 
## Reading items.csv file
with open('items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='hashes')
    for row in reader:
        print(row)
 
## Appending a line to the csv file
with open('items.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, dialect='hashes')
    writer.writerow(('spoon', 3, 1.5))