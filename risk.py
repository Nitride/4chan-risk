import random
import sys
import os

#below is basic 

name=str(input('Name:')) #user inputs
bonus=int(input('Bonus:'))
action=str(input('Roll:'))
roll=random.randrange(0,1000) #rolls random 3 digit number

if roll<100: #adds 0s to rolls that aren't 3 digits
    rolldig='0'+str(roll)
    if roll<10:
        rolldig='00'+str(roll)
else:
    rolldig=str(roll)

print(name,'[+',bonus,']:',action,'\n',rolldig) #posts input info and roll

rollval1=int(rolldig[-1]) #gets digits of roll
rollval2=int(rolldig[-2])
rollval3=int(rolldig[-3])

if rollval1==rollval2==rollval3:
    print('trips!')
    rollpnt=20 #trips = 20
    print(rollpnt + bonus, 'Ts') #adds roll points and bonus
else:
    if rollval1==rollval2!=rollval3:
        print('dubs!')
        rollpnt=10 #dubs = 10
        print(rollpnt + bonus, 'Ts')
    elif rollval1 <= 3:
        if rollval1 != 0:
            rollpnt = 2 #1-3 = 2
            print(rollpnt + bonus, 'Ts')
        else:
            rollpnt = 8 #0 = 8
            print(rollpnt + bonus, 'Ts')
    elif rollval1 > 3:
        if rollval1 <= 6:
            rollpnt = 4 #4-6 = 4
            print(rollpnt + bonus, 'Ts')
        else:
            rollpnt = 6 #7-9 = 6
            print(rollpnt + bonus, 'Ts')

'''
1-3=2
4-6=4
7-9=6
0=8
dubs=10
trips=20

cal = 20 ts
ore = 10 ts
was = 5 ts
'''
#all below is a work in progress

Ts=rollpnt+bonus

if action in ['cal']: #cal fill
    if Ts>20:
        print('cal filled')
        calleft=0
        calspill=Ts-20
        print(calspill, 'spill from cal')
        if str(input('spill where?:')) in ['ore']: #ore fill
            oreleft = 10 - calspill
            if oreleft > 0:
                print(oreleft, 'left in ore')
                wasleft = 5
                wasspill = 0
            else:
                print('ore filled')
                orespill = calspill - 10
                print (orespill, 'spill from ore' ) #end ore fill
                if str(input('spill where?:')) in ['was']: #was fill
                    wasleft = 5 - orespill
                    if wasleft > 0:
                        print(wasleft, 'left in was')
                        wasspill = 0
                    else:
                        print('was filled')
                        wasspill = orespill - 5
                        print(wasspill, 'spill from was') #end was fill
    else:
        calleft=20-Ts
        oreleft=10
        wasleft=5
        wasspill=0
        print(calleft, 'left in Cal') #end cal fill
print('My territory:',
      20-calleft, 'in cal;',
      10-oreleft, 'in ore;',
      5-wasleft,'in was;',
      wasspill, 'spill;')