import random
import numpy
count = 0
a = 0
ave = 0
numberofTimes = 1
#methods
def generateRandomPoint():
    return random.uniform(-1,1)
def addVector(vec1, vec2):
    a = len(vec1)
    i = 0
    vec3 = [None]*a
    for item in vec1:
        vec3[i] = item + vec2[i]
        i+=1
    return vec3
def dot(vec1, vec2):
    result = 0
    a = len(vec1)
    i = 0
    vec3 = [None]*a
    for item in vec1:
        result+= (item*vec2[i])
        i+=1
    return result
    #[1,x,y]
#setup
int =random.uniform(-1,1)
firstX = random.uniform(-1,1)
firstY= random.uniform(-1,1)
secondX= random.uniform(-1,1)
secondY= random.uniform(-1,1)
slope = (secondY - firstY)/(secondX-firstX)
initialLine = [slope, -1, int]
i = 100 #(int(input("how many datapoints do you want? ")))
xList = [None]*i
yList = [None]*i
answerList = [None]*i
potentialList = [None]*i
while a <len(xList):
    xList[a] = generateRandomPoint()
    yList[a] = generateRandomPoint()
    a = a+1
a = 0
while a < len(xList):
    place = xList[a]
    placetwo =yList[a]
    placevec = [place, placetwo, 1]
    if (dot(placevec,initialLine) >=0):
        answerList[a] = True
        a = a+1
    else:
        answerList[a] = False
        a = a+1
a = 0
#print(answerList)
#print('')
#ML stuff
#print(answerList)
int2 = random.uniform(-1,1)
thirdX= random.uniform(-1,1)
thirdY= random.uniform(-1,1)
fourthX= random.uniform(-1,1)
fourthY = (random.uniform(-1,1))
slopeTwo = (fourthY-thirdY)/(fourthX-thirdX)
testvec = [slopeTwo, -1, int2]
iterations = 0
while(iterations<10):
    while(True):
        while a < len(xList):
            place = xList[a]
            placetwo =yList[a]
            placevec = [place, placetwo, 1]
            if (dot(placevec,testvec) >=0):
                potentialList[a] = True
                a = a+1
            else:
                potentialList[a] = False
                a = a+1
      #  print(potentialList)
        a = 0
        while a < len(xList):
            if answerList[a] != potentialList[a]:
                break
            else:
                a = a+1
        if(a ==len(xList)):
            ave = ave + numberofTimes
            break
            #[x,y,1]
        if answerList[a] == False:
            pl = ((-1) * (xList[a]))
            pltwo =((-1) *(yList[a]))
            plvec = [pl, pltwo, -1]
            testvec = addVector(testvec,plvec)
        if answerList[a] == True:
            pl =(xList[a])
            pltwo =(yList[a])
            plvec = [pl, pltwo, 1]
            testvec = addVector(testvec,plvec)
        a = 0
        numberofTimes = numberofTimes+1  
    #print(ave)
   #print(iterations)
    iterations = iterations+1
   # print(numberofTimes)

   # numberofTimes = 0
   #potentialList = [None]*i
    #int2 = random.uniform(-1,1)
    #thirdX= random.uniform(-1,1)
    #thirdY= random.uniform(-1,1)
    #fourthX= random.uniform(-1,1)
    #fourthY = (random.uniform(-1,1))
    #slopeTwo = (fourthY-thirdY)/(fourthX-thirdX)
    #testvec = [slopeTwo, -1, int2]
#print(f"Completed in {numberofTimes} iterations")

#print(ave/10000)


      #code to determine probability
    xList2 = [None]*10000
    yList2 = [None]*10000
    answerList2 = [None]*10000
    potentialList2 = [None]*10000
    a = 0
    while a <len(xList2):
        xList2[a] = generateRandomPoint()
        yList2[a] = generateRandomPoint()
        a = a+1
    a = 0
    while a < len(xList2):
        place = xList2[a]
        placetwo =yList2[a]
        placevec = [place, placetwo, 1]
        if (dot(placevec,testvec) >=0):
            potentialList2[a] = True
            a = a+1
        else:
            potentialList2[a] = False
            a = a+1
    a = 0
    while a < len(xList2):
        place = xList2[a]
        placetwo =yList2[a]
        placevec = [place, placetwo, 1]
        if (dot(placevec,initialLine) >=0):
            answerList2[a] = True
            a = a+1
        else:
            answerList2[a] = False
            a = a+1
    a = 0
    while(a < len(xList2)):
        if(answerList2[a] != potentialList2[a]):
            count = count + 1
        a= a+1
    numberofTimes = 1
    potentialList = [None]*i
    int2 = random.uniform(-1,1)
    thirdX= random.uniform(-1,1)
    thirdY= random.uniform(-1,1)
    fourthX= random.uniform(-1,1)
    fourthY = (random.uniform(-1,1))
    slopeTwo = (fourthY-thirdY)/(fourthX-thirdX)
    testvec = [slopeTwo, -1, int2]
print(count/1000000)


#print(numberofTimes)
#print(answerList)
#        
    
        
    
    
