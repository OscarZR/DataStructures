'''
I this program we built a hash table using the chaining scheme in a
telephone schedule, we call instructions: add,check,find and del.
For each instruction "check" we print the array of strings saved at that
moment in that specific index, and for each "find" instruction we search
for the calculated hash value of the given string in our table and we print 
"yes" if its on the table or "no" if not.
For calculate the hash value of each string:
Let S be the arrangement of the ascii codes of each of our letters in the
string, we do hashing like:
    
    h(S) = ((sum(S[i]*x**i)) mod p) mod m   ,   i from 0 to len(S)-1
    
where m is the size of our hash table and p is a larger prime number,
in this case p = 1000000007.
And our hash table will be a dinamic array of lenght m.

In this script we use a toy example '1.txt':
5
12
add world
add HellO
check 4
find World
find world
del world
check 4
del HellO
add luck
add GooD
check 2
del good

And the program must print:
HellO world
no
yes
HellO 
GooD luck

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
        b = hashp[mm][::-1]             #Inverted array
        return " ".join(b)
    
    else: pass


if __name__ == '__main__':
    prime = 1000000007
    x = 263
    
    f = open("01.txt", "r")             #Toy example
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
    
    
    
