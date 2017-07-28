from __future__ import division
from itertools import product
from math import ceil
import random 

def catnumber(n):
    ans = 1.0
    for k in range(2,n+1):
     ans = ans *(n+k)/k
    return int(ans)


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


for i in range(1,30):
    print str(i)+': ',getNumbOfIsomorphic3Angulation(i+2)
