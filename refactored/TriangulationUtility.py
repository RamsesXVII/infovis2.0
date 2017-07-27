from __future__ import division
from itertools import product
from math import ceil
import random 
from scipy.stats import chisquare

class TriangulationUtility:

	def __init__(self,polygonNodes):

		self.polygonNodes=polygonNodes
		self.polygon=self.getPolygonTuple(polygonNodes)


	def getCatalanNumber(self,n):
	    return self.catnumber(n-2)

	def catnumber(self,n):
	    ans = 1.0

	    for k in range(2,n+1):
			ans = ans *(n+k)/k

	    return int(ans)

	def getPolygonTuple(self,polygonNodes):
	    tupleToReturn=tuple()

	    for i in range(1,self.polygonNodes+1):
	        tupleToReturn=tupleToReturn+tuple(str(chr(i)))

	    return tupleToReturn

	def getNthTriangulation(self,pl,randInt):
		"""Generate the nth (randInt) triangulations of the convex polygon pl.
		The sequence pl consists of the vertices of the polygon.
		Each triangulation in the output is a list of triangles, and each
		triangle is a tuple of three vertices.

		>>> list(triangulations(tuple('abcd')))
		[[('a', 'b', 'd'), ('b', 'c', 'd')], [('a', 'b', 'c'), ('a', 'c', 'd')]]
		>>> [sum(1 for _ in triangulations(range(i))) for i in range(3, 8)]
		[1, 2, 5, 14, 42]
		Original code on http://garethrees.org/2013/06/15/triangulation/
		"""
		result = []
		n = len(pl)
		if n == 2:
		     result.append([])
		elif n == 3:
		     result.append([pl])
		else:
		    counter=0

		    for k in range(1, n - 1):
		        leftT=pl[:k + 1]
		        rightT=pl[k:]

		        leftCat=self.getCatalanNumber(len(leftT))
		        rightCat=self.getCatalanNumber(len(rightT))

		        prodOfCat=leftCat*rightCat

		        if randInt<=(prodOfCat+counter):
		            delta=randInt-counter
		            randLeft=ceil(delta/rightCat)
		            randRight=int(delta%rightCat)

		            if(randRight==0):
		                randRight=rightCat

		            for u, v in product(self.getNthTriangulation(leftT,randLeft), self.getNthTriangulation(rightT,randRight)):
		                result.append( u + [(pl[0], pl[k], pl[-1])] + v)

		            
		            return result

		        else:
		            counter+=prodOfCat

		return result