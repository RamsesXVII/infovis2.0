from __future__ import division
from itertools import product
from math import ceil
import random 
from scipy.stats import chisquare
from ChiSquaredUtility import *
from TriangulationUtility import *

class RandomOuterplanarGenerator:

	def __init__(self,polygonNodes):
		self.triangulationUtility=TriangulationUtility(polygonNodes)
		self.chiSquaredUtility=ChiSquaredUtility(polygonNodes)

		self.polygonNodes=polygonNodes
		self.catalanNumber=self.triangulationUtility.getCatalanNumber(polygonNodes)

		self.triangulationToCount=dict()
		self.triangulationToDegreeSequence=dict()


	def getTriangulationUniformlyAtRandom(self):
		'''It generates an uniformly at random triangulation in the form of a sequence of triangles. Each triangle is
		a triple of symbol and each symbol is associated with a vertex. It supports a max of 255 vertex because it s performed
		a conversion from a number to its respective ASCII value. '''
		notFound=True

		while(notFound):
			randInt=random.randint(1,self.catalanNumber)

			polygon=self.triangulationUtility.getPolygonTuple(self.polygonNodes)
			#to peform a specific triangulation use  polygon=list(tuple("123456789"))
			tr=self.triangulationUtility.getNthTriangulation(polygon,randInt)

			randomTriangulation=tr[0]
			isomorphicCount=self.chiSquaredUtility.getIsomorphicCount(randomTriangulation)
			normalizer=random.randint(1,isomorphicCount)

			if(normalizer==1):
				notFound=False

		return randomTriangulation

	def generateRandomGraphNtimes(self,observationNumber):
		'''It generates n random graph. Each graph is first associated with its identical copies,
		then it's performed an isomorphic validation to aggregate the count with its isomorphic copies.
		Finally it's printed the chi squared score in order to check the coorrect distribution of value.'''
		for j in range (0,observationNumber):
			randomTriangulation=self.getTriangulationUniformlyAtRandom()

			if str(randomTriangulation) in self.triangulationToCount:
				self.triangulationToCount[str(randomTriangulation)]+=1
			else:
				self.triangulationToCount[str(randomTriangulation)]=1
				self.triangulationToDegreeSequence[str(randomTriangulation)]=self.chiSquaredUtility.getDegreeSequence(randomTriangulation)

		notIsomorphicToCount=self.chiSquaredUtility.aggregateByIsomorphism(self.triangulationToCount,self.triangulationToDegreeSequence)
		chiSquaredAndDegreeToCount=self.chiSquaredUtility.getChiSquared(observationNumber,notIsomorphicToCount)

		return(chiSquaredAndDegreeToCount)