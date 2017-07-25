from __future__ import division
from itertools import product
from math import ceil
import random 
from scipy.stats import chisquare

def C(n):
    if(isinstance(n,int)):
        return catnumber(n)
    
    return catnumber(int(round(n)))

def getNumbOfIsomorphic3Angulation(n):
    if(n%2==0):
        k=1
    else:
        k=0
    if(n%3==0):
        j=1
    else:
        j=0

    inside=C(n-2)+k*(3*n)/2*C(n/2-1)+(1-k)*n*C((n-3)/2)+j*(2*n)/3*C((n/3)-1)
    numb=1/(2*n)*(inside)
    return numb

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
    for triangle in triangulation:
        for node in triangle:
            if node in nodeToCount:
                nodeToCount[node]+=1
            else:
                nodeToCount[node]=2

    degreeSequence=list()
    for node in sorted(nodeToCount.keys()):
        degreeSequence.append(nodeToCount[node])

    return degreeSequence



def getIsomorphicCount(randomTriangulation,polygonNodes):
    nodeToCount=dict()
    for triangle in randomTriangulation:
        for node in triangle:
            if node in nodeToCount:
                nodeToCount[node]+=1
            else:
                nodeToCount[node]=2

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
