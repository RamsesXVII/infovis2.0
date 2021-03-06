from itertools import product
from math import ceil
import random 

def isIsomorphic(degSeq1,degSeq2,polygonNodes):

    degreeSequenceSet=set()
    degreeSequenceSet.add(str(degSeq1))

    for i in range (1,polygonNodes):
        degreeSequenceSet.add(str(shiftRight(degSeq1,i)))

    if str(degSeq2) in degreeSequenceSet:
        return True

    if  str(degSeq2[::-1]) in degreeSequenceSet:
        return True

    return False




def getDegreeSequence(triangulation):
    nodeToCount=dict()
    for triangolo in randomTriangulation:
        for nodo in triangolo:
            if nodo in nodeToCount:
                nodeToCount[nodo]+=1
            else:
                nodeToCount[nodo]=2

    degreeSequence=list()
    for node in sorted(nodeToCount.keys()):
        degreeSequence.append(nodeToCount[node])

    return degreeSequence



def getIsomorphicCount(randomTriangulation):
    nodeToCount=dict()
    for triangolo in randomTriangulation:
        for nodo in triangolo:
            if nodo in nodeToCount:
                nodeToCount[nodo]+=1
            else:
                nodeToCount[nodo]=2

    degreeSequence=list()
    for node in sorted(nodeToCount.keys()):
        degreeSequence.append(nodeToCount[node])

    degreeSequenceSet=set()
    degreeSequenceSet.add(str(degreeSequence))

    for i in range (1,polygonNodes):
        degreeSequenceSet.add(str(shiftRight(degreeSequence,i)))

    eqRotations=len(degreeSequenceSet)
    mirroredDegree=str(degreeSequence[::-1])

    if mirroredDegree not in degreeSequenceSet:
        eqRotations=eqRotations*2
    return eqRotations

def getPolygonTuple(polygonNodes):
    tupleToReturn=tuple()
    for i in range(1,polygonNodes+1):
        tupleToReturn=tupleToReturn+tuple(str(chr(i)))

    return tupleToReturn

def shiftRight(listToRotate,n):
    return listToRotate[-n:]+listToRotate[:-n]

def getCatalanNumber(n):
    return catnumber(n-2)

def catnumber(n):
    ans = 1.0
    for k in range(2,n+1):
     ans = ans *(n+k)/k
    return int(ans)

def triangulations(p,randInt):
    result = []
    n = len(p)
    if n == 2:
         result.append([])
    elif n == 3:
         result.append([p])
    else:
        counter=0

        for k in range(1, n - 1):
            leftT=p[:k + 1]
            rightT=p[k:]

            leftCat=getCatalanNumber(len(leftT))
            rightCat=getCatalanNumber(len(rightT))

            prodOfCat=leftCat*rightCat

            if randInt<=(prodOfCat+counter):
                delta=randInt-counter
                randLeft=ceil(delta/rightCat)
                randRight=int(delta%rightCat)

                if(randRight==0):
                    randRight=rightCat

                for u, v in product(triangulations(leftT,randLeft), triangulations(rightT,randRight)):
                    result.append( u + [(p[0], p[k], p[-1])] + v)

                
                return result

            else:
                counter+=prodOfCat
    return result

counter=0
for contatore in range(6,15):
    conttoreEstrazioni=0
    polygonNodes=contatore
    print(polygonNodes)
    print("ooooooooooooooooooooooooooooooooo")
    exToCount=dict()
    exToDegreeSequence=dict()

    for j in range (0,50000):
        nonTrovato=True

        while(nonTrovato):
            conttoreEstrazioni+=1
            counter+=1
            randInt=random.randint(1,getCatalanNumber(polygonNodes))

            polygon=getPolygonTuple(polygonNodes)
            tr=triangulations(polygon,randInt)

            randomTriangulation=tr[0]
            isomorphicCount=getIsomorphicCount(randomTriangulation)
            normalizer=random.randint(1,isomorphicCount)
            if(normalizer==1):
                nonTrovato=False
                if str(randomTriangulation) in exToCount:
                    exToCount[str(randomTriangulation)]+=1
                else:
                     exToCount[str(randomTriangulation)]=1
                     exToDegreeSequence[str(randomTriangulation)]=getDegreeSequence(randomTriangulation)




    notIsomorphicToCount=dict()

    for t in exToCount:
        tFound=False
        degreeSeqOft=exToDegreeSequence[str(t)]

        for nI in notIsomorphicToCount:
            listOfInteger=list()
            for integ in nI.split(","):
                listOfInteger.append(int(integ))
            if isIsomorphic(degreeSeqOft,listOfInteger,polygonNodes):
                notIsomorphicToCount[nI]+=exToCount[t]
                tFound=True
                break
        if(tFound==False):
            notIsomorphicToCount[str(degreeSeqOft)[1:-1]]=exToCount[t]

    for t in notIsomorphicToCount:
        print(str(t)+","+str(notIsomorphicToCount[t]))

    print(len(notIsomorphicToCount))
    print("estrazioni "+str(conttoreEstrazioni))
