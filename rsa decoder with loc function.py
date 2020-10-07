import sys
import math

def power_mod(a,n,m): #exodos a^n modm
	x=a%m
	y=1
	while(n>0):
		if(n%2!=0):
			y = (y*x)%m
		x = (x*x)%m
		n = n//2
	return y

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

p= 16816861
q= 64678841
n=p*q
e = 515174682635987
phi = (p-1)*(q-1)

gcd, a, b = egcd(e, phi)
d = a


def encr(m, e, n):
	return power_mod(m, e, n)


########################################################

def oracle(ct):
	#decrypt with private key d
	m = power_mod(ct, d, n)
	#print("m is ", m)
	return(m > n/2)

######################################################
def attack(og_ct, ct, e, n, l, r):
	if r>l:
		mid = (r+l)//2
		print(l, r, mid)
		if r-l<=3:
			#print(l,r)
			for i in range(l,r+1):
				if encr(i, e, n) == og_ct:
					return i

		if oracle(ct):
			return attack(og_ct, ct * encr(2, e, n), e, n, mid-1, r)
		else:
			return attack(og_ct, ct * encr(2, e, n), e, n, l, mid+1)

	else:
		return r #not needed tbh

##################################################

m = 97649
ct = encr(m, e, n)
print( attack(ct, ct, e, n, 0, n) == m)
