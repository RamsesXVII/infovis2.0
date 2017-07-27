import sys
partialSum=[]

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    if s == target and len(partial)==3: 
        partialSum.append(partial)
    if s >= target:
        return  

    for i in range(len(numbers)):
        n = numbers[i]
        orderedPartial=partial + [n]
        orderedPartial.sort()
        subset_sum(numbers, target, orderedPartial) 

def gendistinct(n):
    leafnode = '(.)'
    dp = []
    newset = set()
    newset.add(leafnode)
    dp.append(newset)
    for i in range(1,n):
        newset = set()
        for j in range(i):
            for leftchild in dp[j]:
                for rightchild in dp[i-j-1]:
                    mom=[]
                    mom.append(leftchild)
                    mom.append(rightchild)
                    mom.sort()
                    newset.add('(' + '.' + mom[0] + mom[1] + ')')
        dp.append(newset)
    return dp[-1]

def getAllPossibleTree():
    hashSum=set()
    for i in partialSum:
        hashSum.add(str(i))

    return hashSum


def getUBTree(n):
    totalList=[]
    h=range(1,(n))
    subset_sum(h,n)
    dp = []
    newset = set()
    count=0
    possibleTree=getAllPossibleTree()
    for subTree in possibleTree:
        subTree=subTree.replace("[","")
        subTree=subTree.replace("]","")
        subTree=subTree.split(",")
        print 'subTree:',subTree
        first= gendistinct(int(subTree[0]))
        second=gendistinct(int(subTree[1]))
        third=gendistinct(int(subTree[2]))
        count=count+1
        for t1 in first:
            for t2 in second:
                for t3 in third:
                    toOrder=[]
                    toOrder.append(t1)
                    toOrder.append(t2)
                    toOrder.append(t3)
                    toOrder.sort()
                    output='('+toOrder[0]+toOrder[1]+toOrder[2]+')'

                    print output
                    totalList.append(output)
    print 'la possibilita sono: '+str(len(totalList))
    #print partialSum
        
        

if __name__ == "__main__":
    getUBTree(int(sys.argv[1]))
    
