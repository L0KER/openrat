#!/usr/bin/python
import os
import sys
print ('You realy reload client and connect scripts?')
print ('1) No, exit')
print ('2) Yes')
a = int(input('openrat>'))
if a > 1:
    print('Ok, enter your old ip')
    drpri = raw_input ('openrat>')
    with open ('client.py', 'r') as f:
      old_data = f.read()

    new_data = old_data.replace(drpri, '127.0.0.1')

    with open ('client.py', 'w') as f:
      f.write(new_data)
    os.rename('client.py', 'client.txt') 

    with open ('connect.py', 'r') as f:
      old_data = f.read()

    new_data = old_data.replace(drpri, '127.0.0.1')

    with open ('connect.py', 'w') as f:
      f.write(new_data)
  
    os.rename('connect.py', 'connect.txt')
    print ('Reloading scripts successful!')
elif a < 2:
    print('Bye!')
