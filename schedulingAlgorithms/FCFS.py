def printWaitingTime(list):
    print('Waiting Time')
    for i in list:
        print (i.get('name'),' ',i.get('ST')-i.get('AT'))
def printTurnAroundTime(list):
    print('Turnaround Time')
    for i in list:
        print (i.get('name'),' ',i.get('FT')-i.get('AT'))


print("This line will be printed.")
with open('input_FCFS.txt') as f:
    lines=f.read().splitlines()
data=[]

for i in lines:
    number_string=i.split();
    numbers=[int(n) for n in number_string]
    data.append(numbers)
temp=['name', 'AT', 'BT']
#for i in lines:
#    for j in temp:
#        keys.append(j)
ready=[]
for i in data:
    ready.append(dict(zip(temp, i)))

sortedReady=sorted(ready,key=lambda k:k['AT'])
print (sortedReady)
time=0

for i in sortedReady:

    if (i.get('AT') > time):
        print('idle=',time,'-',i.get('AT'))
        time = i.get('AT')
    i['ST']=time
    print('p',i.get('name'),'=',time,'-',time+i.get('BT'))
    time+=i.get('BT')
    i['FT']=time
print(sortedReady)
printWaitingTime(sortedReady)
printTurnAroundTime(sortedReady)
