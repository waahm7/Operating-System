def printWaitingTime(list):
    print('Waiting Time')
    for i in list:
        print (i.get('name'),' ',i.get('ST')-i.get('AT'))
def printTurnAroundTime(list):
    print('Turnaround Time')
    for i in list:
        print (i.get('name'),' ',i.get('FT')-i.get('AT'))


print("This line will be printed.")
with open('input_RR.txt') as f:
    lines=f.read().splitlines()
data=[]
for i in lines:
    number_string=i.split();
    numbers=[int(n) for n in number_string]
    data.append(numbers)
timeQuantam=data[0][0]
print(timeQuantam)
del(data[0])

temp=['name', 'AT', 'BT']
#for i in lines:
#    for j in temp:
#        keys.append(j)
ready=[]
for i in data:
    ready.append(dict(zip(temp, i)))

sortedReady=sorted(ready,key=lambda k:k['AT'])
readyQueue=[]
finished=[]
print (sortedReady)
time=0
while len(sortedReady)!=0 or len(readyQueue)!=0:
        print('here')
        while (len(sortedReady) > 0 and sortedReady[0].get('AT') <= time):
            readyQueue.append(sortedReady[0])
            del (sortedReady[0])
        if(len(readyQueue)<1):
            time+=1
            continue

        if(readyQueue[0].get('ST',-1)==-1):
            readyQueue[0]['ST']=time
        if readyQueue[0].get('BT')>timeQuantam:
            print('p', readyQueue[0].get('name'), '=', time, '-', time + timeQuantam)
            time += timeQuantam
            temp=readyQueue[0]
            temp['BT']=temp['BT']-timeQuantam
            del(readyQueue[0])
            while (len(sortedReady) > 0 and sortedReady[0].get('AT') <= time):
                readyQueue.append(sortedReady[0])
                del (sortedReady[0])
            readyQueue.append(temp)
        else:
            print('p', readyQueue[0].get('name'), '=', time, '-', time + readyQueue[0].get('BT'))
            time += readyQueue[0].get('BT')
            readyQueue[0]['FT'] = time
            finished.append(readyQueue[0])
            del (readyQueue[0])

print(finished)
printWaitingTime(finished)
printTurnAroundTime(finished)
