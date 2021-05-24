# python3
'''
In this program, you can input a string s, followed by a sequence of n triplets
of integers: [a,b,l], a must be the index where yor first substring is going 
to begin, b is the index where yor second substring is going to begin and l is 
the length of both substring. The program must print for each n triplets "yes" 
if the substrings are equal or "no" if not.
Here, we precompute first each of the letters of the string s using hash
function:
    
    h1[i] = (x*h[i-1] + s[i])%p1
    h2[i] = (x*h[i-1] + s[i])%p2
    
where p1 and p2 are two differents big prime numbers, (in this case 1000000007
and 1000000009), the s[i] are the ascii code of each of the letters of s and
x is an integer x=263.

then, in the solver() function we compare for each n triplet, the mod p of the 
polynomial sum of each of the hash values in both substrings, like:
    
    v1 = (h1[a+l] - h1[a]*x^l)%p1
    v2 = (h1[b+l] - h1[b]*x^l)%p1
    
we compare both calculated values v, and, if are equal, we do it again but
using p2 and precompute values h2 for avoiding collisions. We can say that
if the values are equal, the substrings are equal, so we print "yes", else
we print "no".

We use pow() function like pow(x,l,p) = (x^l)%p to avoid integer overflow.
'''
import sys

def solver(aa,bb,ll):
    y = pow(x,ll,prime1)   
    gr1 = (hash1[aa+ll] - (y*hash1[aa]))%prime1
    fr1 = (hash1[bb+ll] - (y*hash1[bb]))%prime1
    
    if gr1 == fr1: #For avoiding collisions
        y = pow(x,ll,prime2)
        gr2 = (hash2[aa+ll] - (y*hash2[aa]))%prime2
        fr2 = (hash2[bb+ll] - (y*hash2[bb]))%prime2        
        if gr2 == fr2: return True    
    return False

#Here we precompute all letters of s
def precomputeH(S):
    ha1,ha2 = [0],[0]
    for i in range(1,len(S)+1):
        ha1.append((x*ha1[i-1]+ord(S[i-1]))%prime1)
        ha2.append((x*ha2[i-1]+ord(S[i-1]))%prime2)
    return ha1,ha2

if __name__ == '__main__':
    prime1,prime2 = int(1e9) + 7,int(1e9) + 9
    x = 263
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    hash1, hash2 = precomputeH(s)

for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver(a, b, l) else "No")
