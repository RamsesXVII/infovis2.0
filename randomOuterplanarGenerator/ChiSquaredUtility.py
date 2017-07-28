from __future__ import division
from itertools import product
from math import ceil
import random 
from scipy.stats import chisquare

class ChiSquaredUtility:

	def __init__(self,polygonNodes):

		self.polygonNodes=polygonNodes


	def C(self,n):
	    if(isinstance(n,int)):
	        return self.catnumber(n)
	    
	    return self.catnumber(int(round(n)))

	def catnumber(self,n):
		ans = 1.0

		for k in range(2,n+1):
			ans = ans *(n+k)/k

		return int(ans)

	def getNumbOfIsomorphicTriangulation(self,n):
	    if(n%2==0):
	        k=1
	    else:
	        k=0
	    if(n%3==0):
	        j=1
	    else:
	        j=0

	    inside=self.C(n-2)+k*(3*n)/2*self.C(n/2-1)+(1-k)*n*self.C((n-3)/2)+j*(2*n)/3*self.C((n/3)-1)
	    numb=1/(2*n)*(inside)
	    return numb

	def isIsomorphic(self,degSeq1,degSeq2):

	    degreeSequenceSet=set()
	    degreeSequenceSet.add(str(degSeq1))

	    for i in range (1,self.polygonNodes):
	        degreeSequenceSet.add(str(self.shiftRight(degSeq1,i)))

	    if str(degSeq2) in degreeSequenceSet:
	        return True

	    if  str(degSeq2[::-1]) in degreeSequenceSet:
	        return True

	    return False

	def getDegreeSequence(self,triangulation):
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



	def getIsomorphicCount(self,randomTriangulation):
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

	    for i in range (1,self.polygonNodes):
	        degreeSequenceSet.add(str(self.shiftRight(degreeSequence,i)))

	    eqRotations=len(degreeSequenceSet)
	    mirroredDegree=str(degreeSequence[::-1])

	    if mirroredDegree not in degreeSequenceSet:
	        eqRotations=eqRotations*2

	    return eqRotations



	def shiftRight(self,listToRotate,n):
	    return listToRotate[-n:]+listToRotate[:-n]


	def aggregateByIsomorphism(self,triangulationToCount,exToDegreeSequence):
	    notIsomorphicToCount=dict()

	    for triangulation in triangulationToCount:
	        ispmorphicIsPresent=False
	        degreeSequence=exToDegreeSequence[str(triangulation)]

	        for classOfIsomorphic in notIsomorphicToCount:
	            listOfInteger=list()
	            for integ in classOfIsomorphic.split(","):
	                listOfInteger.append(int(integ))
	            if self.isIsomorphic(degreeSequence,listOfInteger):
	                notIsomorphicToCount[classOfIsomorphic]+=triangulationToCount[triangulation]
	                ispmorphicIsPresent=True
	                break
	        if(ispmorphicIsPresent==False):
	            notIsomorphicToCount[str(degreeSequence)[1:-1]]=triangulationToCount[triangulation]

	    return notIsomorphicToCount

	def getChiSquared(self,observationNumber,notIsomorphicToCount):
	    expected=list()
	    observed=list()

	    notIsorphicCount=int(self.getNumbOfIsomorphicTriangulation(self.polygonNodes))

	    for i in range(1,notIsorphicCount+1):
	        expected.append(round(observationNumber/notIsorphicCount,3))

	    degreeSequenceToCount=list()

	    for t in notIsomorphicToCount:
	        observed.append(int(notIsomorphicToCount[t]))
	        degreeSequenceToCount.append(str(t)+","+str(notIsomorphicToCount[t]))

	    return (chisquare(observed, f_exp=expected), degreeSequenceToCount)