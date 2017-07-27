from RandomGenerator import *
import sys

class OuterplanarGenerator(object):
	def __init__(self, minPolygonSize, maxPolygonSize, extractionCount):
		self.maxPolygonSize = int(maxPolygonSize)
		self.minPolygonSize= int(minPolygonSize)
		self.extractionCount = int(extractionCount)

	def generateRandomOuterplanarNtimes(self):

		observationNumber=self.extractionCount
		for polygonNodes in range(self.minPolygonSize,self.maxPolygonSize+1):    
		    print("Generation of "+str(observationNumber)+" maximal outerplanar graphs of "+str(polygonNodes)+ " nodes")
		    
		    rGenerator=RandomOuterplanarGenerator(polygonNodes)
		    chiSquaredAndDegreeToCount=rGenerator.generateRandomGraphNtimes(observationNumber)

		    print(chiSquaredAndDegreeToCount[0])
		    print(chiSquaredAndDegreeToCount[1])

	def generateRandomOuterplanar(self):

	    rGenerator=RandomOuterplanarGenerator(self.maxPolygonSize)
	    randomGraph=rGenerator.getTriangulationUniformlyAtRandom()

	    print(randomGraph)

if  __name__ =='__main__':
	generationType=sys.argv[1]

	if(generationType=="S"):
		polygonSize=sys.argv[2]

		outerplanarGenerator = OuterplanarGenerator(polygonSize, polygonSize, 1)    
		outerplanarGenerator.generateRandomOuterplanar()

	elif(generationType=="M"):
		minPolygonSize=sys.argv[2]
		maxPolygonSize=sys.argv[3]
		extractionCount=sys.argv[4]

		outerplanarGenerator = OuterplanarGenerator(minPolygonSize, maxPolygonSize,extractionCount)    
		outerplanarGenerator.generateRandomOuterplanarNtimes()
	
	else:
		print("Please enter valid parameters")