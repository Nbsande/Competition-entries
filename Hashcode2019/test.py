import random
from copy import deepcopy
import numpy as np
with open('c_medium.in','r') as f:
    IN=[x.rstrip() for x in f.readlines()]
n=[int(x) for x in IN.pop(0).split(" ")]

Min=0
Pizza=[]

for i in range(len(IN)):
    pizzaRow=[]
    for j in range(len(IN[0])):
        pizzaRow.append(IN[i][j])
        Min=Min+1
    Pizza.append(pizzaRow)
    
allowedSliceShapes=[]
def defPizza():
    global pizza
    pizza=Pizza.copy()
    
    return pizza
IN=None

for i in range(2,1+int(n[3]/2)):
    
    j=i
    while j<(1+n[3]/2):
        #print(f'currently {i} {j}')
        if i*j<=n[3]:
            allowedSliceShapes.append((i,j))
            if i!=j:
                allowedSliceShapes.append((j,i))
        j=j+1

def GetNewPosition():
    done=False
    while not done:
        pos=(random.randint(0,n[0]-1),random.randint(0,n[1]-1))
        if pizza[pos[0]][pos[1]]!=0:
            done=True
    return pos

def sliceCheck(shape,currentPos):
    global pizza
    if shape[0]+currentPos[0]>len(pizza) or shape[1]+currentPos[1]>len(pizza[0]):
        #print(f'EDGE? {shape[0]+currentPos[0]} {shape[1]+currentPos[1]}')
        return False
    Mcount=0
    Tcount=0
    for i in range(shape[0]):
        for j in range(shape[1]):
            #print(f'Position {currentPos[0]+i} {currentPos[1]+j}')
            if pizza[currentPos[0]+i][currentPos[1]+j]==0:
                return False
            if pizza[currentPos[0]+i][currentPos[1]+j]=="M":
                Mcount=Mcount+1
            if pizza[currentPos[0]+i][currentPos[1]+j]=="T":
                Tcount=Tcount+1
    if (Mcount<n[2]) or (Tcount<n[2]) or (Mcount>n[3]) or (Tcount>n[3]):
        return False
    #print('sliced')
    return True
    


def sliceSelect(currentPos):
    for shape in allowedSliceShapes:
        if(sliceCheck(shape,currentPos)):
            return shape
    return False

def MakeZero(shape,currentPos):
    global pizza
    for i in range(shape[0]):
        for j in range(shape[1]):
            pizza[currentPos[0]+i][currentPos[1]+j]=0
    
def BruteForce():
    slices=[0]
    failCount=0
    while failCount<30:
        currentPos=GetNewPosition()
        shape=sliceSelect(currentPos)
        if shape:
            MakeZero(shape,currentPos)
            shapeSlice=[currentPos[0],currentPos[1],currentPos[0]+shape[0]-1,currentPos[1]+shape[1]-1]
            slices.append(shapeSlice)
            slices[0]=slices[0]+1
            failCount=0
            #print('worked')
        else:
            failCount=failCount+1
    return slices

def CleanUp(slices):
    global pizza
    rowLen=len(pizza[0])-1
    #print(rowLen)
    for i in range(len(pizza)):
        done=False
        rowItem=0
        if i!=len(pizza)-1:
            while not done:
                #print(f' {i} {rowItem} ')
                if rowItem<=rowLen-1:
                    if pizza[i][rowItem]!=0:
                        if pizza[i][rowItem+1]!=0:
                            if pizza[i+1][rowItem+1]!=0:
                                if pizza[i+1][rowItem]!=0:
                                    shape=sliceSelect((i,rowItem))
                                    if shape:
                                        MakeZero(shape,(i,rowItem))
                                        shapeSlice=[i,rowItem,i+shape[0]-1,rowItem+shape[1]-1]
                                        slices.append(shapeSlice)
                                        slices[0]=slices[0]+1
                                        


                    rowItem=rowItem+1
                else:
                    done=True    
    return slices

def leftOverCount():
    global pizza
    leftCount=0
    for i in pizza:
        for j in i:
            if j!=0:
                leftCount=leftCount+1
    return leftCount
print('Min',end=" ")
print(Min)

def main(Min=Min):
    for k in range(5000):
        slices=[0]
        global pizza
        pizza=deepcopy(Pizza)
        slices=BruteForce()
        slices=CleanUp(slices)
        leftCount=leftOverCount()
        if Min>=leftCount:
            Min=leftCount
            print("\n"+str(leftCount))
            #print(pizza)    
       
    print(slices)
    with open("medium.out",'w') as f:
        for n in slices:
            f.write(n)

main()