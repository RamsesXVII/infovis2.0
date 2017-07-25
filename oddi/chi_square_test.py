from  random_tringulation_generator import *


counter=0
observationNumber=50000
for polygonNodes in range(6,7):
    conttoreEstrazioni=0
    
    print(polygonNodes)
    print("ooooooooooooooooooooooooooooooooo")
    exToCount=dict()
    exToDegreeSequence=dict()

    for j in range (0,observationNumber):
        nonTrovato=True

        while(nonTrovato):
            conttoreEstrazioni+=1
            counter+=1
            randInt=random.randint(1,getCatalanNumber(polygonNodes))

            polygon=getPolygonTuple(polygonNodes)
            tr=triangulations(polygon,randInt)

            randomTriangulation=tr[0]
            isomorphicCount=getIsomorphicCount(randomTriangulation,polygonNodes)
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

    observed=list()
    notIsorphicCount=int(getNumbOfIsomorphic3Angulation(polygonNodes))
    expected=list()

    for i in range(1,notIsorphicCount+1):
        expected.append(round(observationNumber/notIsorphicCount,3))

    
    for t in notIsomorphicToCount:
        observed.append(int(notIsomorphicToCount[t]))
        print(str(t)+","+str(notIsomorphicToCount[t]))
    print(chisquare(observed, f_exp=expected))
    print(observed)
    print(len(observed))
    print(expected)
    print(len(expected))
    print(len(notIsomorphicToCount))
    print("estrazioni "+str(conttoreEstrazioni))
