import datetime,random

def getBirthdays(numberOfBirthdays):
    birthdays=[]

    for i in range(numberOfBirthdays):
        startOfYear=datetime.date(2001, 1, 1)
        #print(startOfYear)

        randomNumberOfDays=datetime.timedelta(random.randint(0, 364))
        #print(randomNumberOfDays)
        birthday=startOfYear+randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getmatch(birthdays):
    if len(birthdays)==len(set(birthdays)):
        return None
    for a, birthdayA in enumerate(birthdays):
        for b,birthdayB in enumerate(birthdays[a+1 :]):
            if birthdayA==birthdayB:
                return birthdayA

print('BirthDay Paradox')

MONTHS=('Jan','Feb','Mar','Apr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dec')

while True:
    print('How many birthdays shall i generate? (Max 100)')
    response=input('> ')
    if response.isdecimal() and (0<int(response)<=100):
        numBdays=int(response)
        break
print()

print('Here are',numBdays,'birhdays:')
birthdays=getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i!=0:
        print(', ',end=' ')
    monthName=MONTHS[birthday.month-1]
    dateText='{} {}'.format(monthName,birthday.day)
    print(dateText,end='')
print()
print()

match=getmatch(birthdays)

print('In this simulation, ',end='')
if match != None:
    monthName=MONTHS[match.month -1]
    dateText='{}{}'.format(monthName,match.day)
    print('Multiple people have a  birthday on ',dateText)
else:
    print('There are no matching birthdays')
print()

print('Generating ',numBdays,'random birthdays 100000 times ...')
input('Press enter to begin')

print('Let\'s run another 100,00 simulations ...')
simMatch=0
for i in range(100_000):
    if i%10_000==0:
        print(i,'simulations run..')
        birthdays=getBirthdays(numBdays)
        if getmatch(birthdays)!=None:
            simMatch=simMatch+1
print('100,000 simulations  run .')
print(simMatch)
probability=round(simMatch/100_000*100,2)
print('Out of 100,000 simulations of', numBdays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')