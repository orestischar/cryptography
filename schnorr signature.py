from hashlib import sha256
from random import randint

def myhashfunction(r, M):
    hash=sha256();
    hash.update(str(r).encode());
    hash.update(M.encode());
    return int(hash.hexdigest(),16);


# generator g
g = 2

# Prime q (for educational purpose I use explicitly a small prime number - for cryptographic purposes this would have to be much larger)
q = 2695139

## Key generation
#Private signing key x
x = 32991
# calculate public verification key y
y = pow(g, x, q)
M = "Tarantino is not good just because he is different"

## Signing
def sign(M, g, q, x):
	k = randint(1, q - 1)
	r = pow(g, k, q)
	e = myhashfunction(r, M) % q 
	s = (k - (x * e)) % (q-1) 
	return (s,e)

## Verification
def verify(M, q, s, e):
	rv = (pow(g, s, q) * pow (y, e, q)) % q
	ev = myhashfunction(rv, M) % q
	if (e == ev):
		print("YUP, that's your signature'")
	else:
		print("IMPOSTER!!")


(s,e) = sign(M, g, q, x)
verify(M, q, s, e)