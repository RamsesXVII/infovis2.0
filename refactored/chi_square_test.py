from RandomGenerator import *

observationNumber=50000
for polygonNodes in range(6,7):    
    print("Estrazione di "+str(observationNumber)+" grafi outerplanar massimali di "+str(polygonNodes)+ " nodi")
    rGenerator=RandomOuterplanarGenerator(polygonNodes)
    chiSquaredAndDegreeToCount=rGenerator.generateRandomGraphNtimes(observationNumber)
    print(chiSquaredAndDegreeToCount[0])
    print(chiSquaredAndDegreeToCount[1])

'''
polygonNodes=9

rGenerator=RandomOuterplanarGenerator(polygonNodes)
print(rGenerator.getTriangulationUniformlyAtRandom())
'''
