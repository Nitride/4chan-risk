import random

#below is basic input and roll functionality

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

print(name,'[+',bonus,']:','moves to',action,'\n',rolldig) #posts input info and roll

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


Ts=rollpnt+bonus #how many territory points player has
fill={'cal':20,'ore':10,'nev':5,'was':5} #how much states are worth
spill=Ts-fill[action] #spill is the difference between T points and state they are filling

while (spill)>0: #loops as long as there is a spill
    print('spill', spill)
    action = input('spill where?:')
    if (spill-fill[action])>=0: #if spill-state fill is at least 0
        print(action, 'filled')
    if (spill-fill[action])<0: #if spill-state fill is less than 0
        print(-1*(spill-fill[action]), 'left in', action)
    spill=spill-fill[action] #redefines spill to old spill-old state filled
if spill==0: #if just enough to fill state
    print(action, 'filled')
elif(spill)<0: #if no spill
    print(fill[action]-Ts, 'left in', action)