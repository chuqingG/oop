import numpy as np
from math import *

def fibo(n):
    '''
    return nth fibonacci number, fibo(1) = fibo(2)=1
    '''
    x_n = 1
    x_m = 1
    for i in range(n-2):
        temp = x_n
        x_n = x_n + x_m
        x_m = temp
    return x_n


def root_5(x):
    '''
    x is a float, use Newton-iteration to get root_5(x)
    '''
    epsilon = 1e-10
    P = [1,0,0,0,0,-x]
    Q = np.polyder(P)
    x = 1
    while(abs(np.polyval(P,x)) >= epsilon):
        x = x - np.polyval(P,x)/np.polyval(Q,x)
    return x

def prime(n):
    '''
    return nth prime number
    '''
    l = []
    l.append(2)
    i = 2
    while(len(l)<n):
        while(1):
            #j = 1
            i = i+1
            for j in range(2,ceil(sqrt(i))+2):
                if i%j == 0:
                    break
            if j == ceil(sqrt(i))+1:
                break
        l.append(i)
    return l[-1]
        
    
def seek_unique(t):
    '''
    parameter t is a list
    return list of item occur only once in t
    '''
    d = {}
    l = []
    for i in t:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    for i in d:
        if(d[i] == 1):
            l.append(i)
    return l

def find_names(s, n):
    '''
    parameter s is a list, which records many names
    parameter n is a name
    return a list involved all names having same initial with n in s
    '''
    re = set()
    for i in s:
        if i[0]==n[0]:
            re.add(i)
    l = list(re)
    return l
