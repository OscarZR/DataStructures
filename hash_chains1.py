#"A la primera" Alejandro el Capo
'''
Sean S el arreglo de los códigos ascii de cada una de nuestras letras en el 
string, hacemos hashing como:
    
    h(S) = ((suma(S[i]*x**i)) mod p) mod m   ,   i de 0 a len(S)-1
    
siendo m el tamaño de nuestra tabla hash y p un número primo mayor 
en este caso p = 1000000007
'''

def function(ha):
    j = 0
    suma = 0
    for a in ha:
        k = ord(a)
        suma +=  k*x**j
        j += 1
    
    return (suma%prime)%m

def search(arr,pal):
    if len(arr) == 0:
        return "NO"
    
    for i in range(len(arr)):
        if arr[i] == pal:
            kk = i
            break
        else: kk = "NO"
    return kk
        
        
def hashing(hash_a):
    if hash_a[0] == "add":
        gr = function(hash_a[1])
        bi = search(hashp[gr],hash_a[1])
        if bi == "NO":
            hashp[gr].append(hash_a[1])
    
    if hash_a[0] == "del":
        gr = function(hash_a[1])
        h = search(hashp[gr],hash_a[1])
        if h != "NO":
            hashp[gr][h] = ""
    
    if hash_a[0] == "find":
        gr = function(hash_a[1])
        h = search(hashp[gr],hash_a[1])
        if h == "NO":
            return "no"
        else:
            return "yes"
    
    if hash_a[0] == "check":
        mm = int(hash_a[1])
        b = hashp[mm][::-1]             #Arreglo invertido
        return " ".join(b)
    
    else: pass


if __name__ == '__main__':
    prime = 1000000007
    x = 263
    
    f = open("01.txt", "r")
    m = int(f.readline())
    n = int(f.readline())
    hashp = [[] for i in range (m)]
    hash_ = []
    for i in range(n):
        hash_.append(f.readline().split())
        it = hashing(hash_[i])
        if it != None:
            print(it)
    f.close()
    
    '''
    m = int(input())
    n = int(input())
    hashp = [[] for i in range (m)]
    hash_ = []
    for i in range(n):
        hash_.append(input().split())
        it = hashing(hash_[i])
        if it != None:
            print(it)
    '''
    
    
