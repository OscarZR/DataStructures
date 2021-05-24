# python3
# Dice si dos substring en una string son iguales usando hash
import sys

def solver(aa,bb,ll):
    y = pow(x,ll,prime1)   
    gr1 = (hash1[aa+ll] - (y*hash1[aa]))%prime1
    fr1 = (hash1[bb+ll] - (y*hash1[bb]))%prime1
    
    if gr1 == fr1:
        y = pow(x,ll,prime2)
        gr2 = (hash2[aa+ll] - (y*hash2[aa]))%prime2
        fr2 = (hash2[bb+ll] - (y*hash2[bb]))%prime2        
        if gr2 == fr2: return True    
    return False
    
def precomputeH(S):
    ha1,ha2 = [0],[0]
    for i in range(1,len(S)+1):
        ha1.append((x*ha1[i-1]+ord(S[i-1]))%prime1)
        ha2.append((x*ha2[i-1]+ord(S[i-1]))%prime2)
    return ha1,ha2

if __name__ == '__main__':
    prime1,prime2 = int(1e9) + 7,int(1e9) + 9
    x = 263
    #s = sys.stdin.readline()
    #q = int(sys.stdin.readline())
    
    s = "trololo"
    hash1, hash2 = precomputeH(s)
    q = 4
    qu = [[0,0,7],[2,4,3],[3,5,1],[1,3,2]]

for i in range(q):
    #a, b, l = map(int, sys.stdin.readline().split())
    a, b, l = qu[i]
    print("Yes" if solver(a, b, l) else "No")
	
    
    
   
