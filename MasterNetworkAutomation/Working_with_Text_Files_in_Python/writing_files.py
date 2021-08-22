#with open('myfile1.txt', 'a') as f:
#    f.write('\nabc\n')
#    f.write('just a 2nd line\n')

with open('configuration.txt', 'r+') as f:
    f.seek(5)
    f.write('100')

    f.seek(10)
    print(f.read(3))