# -*- coding: utf-8 -*-
"""
Rope data structure using splay tree.
This rope implementation stores a single CHARACTER (not a string) in each node.

The script implements the rope ds and the find, split, splay and merge operations, which can be used to implement other operations.

The script receives a string and creates the rope, and then an integer n of the number of instructions to receive.
After that it receives n three digit (i,j,k) instructions to take a slice of the string from i to j and then insert 
it at position k in the remaining string.

Returns the remaining string after the n operations

theolivetrees
3
5 5 0
5 5 1
2 4 5
ilovethetrees

@author: villacuPC
"""
import random 

class Node:
    def __init__(self,size, left, right, parent,ch=''):
        (self.key, self.size, self.left, self.right, self.parent) = (ch, size, left, right, parent)

def update(v):
    '''
    Used in merge, split and rotation operations
    '''
    if v == None:
        return
    v.size = 1 + (v.left.size if v.left != None else 0) + (v.right.size if v.right != None else 0)
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v

def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else: 
            grandparent.right = v


def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)    
  else: 
    # Zig-zag
    smallRotation(v)
    smallRotation(v)


def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v
    
def OStat(R,k):
    '''
    Find (order statistic version)
    Iterative version
    
    Parameters
    ----------
    root : root
    key : TYPE
        DESCRIPTION.

    Returns
    -------
    R node found
    '''
    if(R==None):
        return None
    CN = R    
    s = ((R.left.size) if (R.left!=None) else 0)
    while (k!=(s+1)):
        if(k<(s+1)):
            CN = CN.left
        elif(k>(s+1)):
            k = k-s-1
            CN = CN.right
        #print('k is {} and s is {}'.format(k,s))
        if(CN==None):
            return None
        else:
            s = ((CN.left.size) if (CN.left!=None) else 0) #inloop
    return CN    
    


def find(root, K):     
    node = OStat(root,K)
    return node

def split(root, k):  
    k = k+1 #for zero-based index
    if(k<1):
        return(None,root)
    result = find(root,k)
    if(result==None):    
        return (root, None)  
    
    right = splay(result)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)

  
def merge(left, right):
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


def createRope(S):
    '''
    merges nodes and then splays random Node
    '''
    root=None
    for i in S:
        root = merge(root,Node(1,None,None,None,i))
        
    #splays random node
    CN = root
    splayN = random.randint(1,len(S)-2)
   # print(splayN)
    for i in range(splayN):
        CN = CN.left
    root = splay(CN)
    return root

def traverseTree(rt):
    '''
    prints in order traversed tree
    '''
    
    CN = rt
    S = [CN] #auxiliary stack
    ans = ''
    if(CN!=None):
        while S:
            while(CN.left!=None):
                CN = CN.left
                S.append(CN)
            aux = S.pop()
            ans += aux.key
            if(aux.right!=None):
                CN = aux.right
                S.append(CN)
    #print(ans)
    return ans

def process(root,i,j,k):
    s1,s2 = split(root,i)
    s2,s3 = split(s2,(j-i)+1)
    s5,s6=split(merge(s1,s3),k)
    root = merge(merge(s5,s2),s6)
    return root

def takeInput():
    S = input()
    root = createRope(S)
    n = int(input())
    for i in range(n):
        i,j,k = [int(i) for i in input().split()]
        root = process(root, i, j, k)
    print(traverseTree(root))
    
if __name__ == "__main__":
    takeInput()

