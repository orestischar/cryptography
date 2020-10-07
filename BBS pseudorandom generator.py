#!/usr/bin/env python3

import sympy
import random
import re 
import sys
import math
import scipy.special as spc
import scipy.stats as sst
import numpy


def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)

def next_usable_prime(x):
        p2 = sympy.nextprime(x)
        while (p2 % 4 != 3):
            p2 = sympy.nextprime(p2)
        return p2

#last prime with 20 binary bits and mod4=3 is 1048571 (there is also 1048573 but mod4=1)

x = random.randint(2**19,1048571-1)
y = random.randint(2**19,1048571-1)

p = next_usable_prime(x)
q = next_usable_prime(y)
M = p*q

N = 16*500000 #since we need 16 bits for every sample
seed = random.randint(2,N-1)
while (seed%p==0 or seed%q==0):
	seed = random.randint(1,N-1)

if (len(sys.argv)>1):
    N=int(sys.argv[1])*16


print ("\np:\t",p)
print ("q:\t",q)

print ("s0:\t",seed)

x = seed
flag = True
og_x = (x*x) % M
bit_output = ""
for i in range(N):
	    x = x*x % M
	    if (x==og_x and i!=0 and flag):
	    	print("period is :\t",i)
	    	flag=False
	    b = x % 2
	    bit_output += str(b)
#print (bit_output)
count=0
for i in range (0, N, 16):
	tetm = bit_output[i:i+8]
	tetag = bit_output[i+8:i+16]
	x_=int(tetm,2)
	y_=int(tetag,2)
	if (math.sqrt((x_-127.5)**2+(y_-127.5)**2) <= 127.5):
		count+=1

print("pi/4 approximation: \t", count / (N//16))
