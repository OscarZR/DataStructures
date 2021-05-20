# python3

'''
Tree class with in-order,pre-Order and post-order traversal.
Iterative implementation
In this implementation, the tree is stored as a list.
Iterative traversal use stacks

This script receives a tree as an input and prints the three traversals.
'''

class TreeOrders:
    def read(self):
        self.n = int(input())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
    def inOrder(self):
        self.result = []
        CN = 0
        S = [CN] 
        while S:
            while(self.left[CN]!=(-1)):
                   CN = self.left[CN]
                   S.append(CN)
            aux = S.pop()
            self.result.append(self.key[aux])
            if (self.right[aux]!=(-1)):
                CN = self.right[aux]
                S.append(CN)
        return self.result

    def preOrder(self):
        self.result = []   
        CN = 0
        S = [CN] 
        while S:
            CN = S.pop()
            self.result.append(self.key[CN])
            if (self.right[CN]!=(-1)):
                S.append(self.right[CN])
            if (self.left[CN]!=(-1)):
                S.append(self.left[CN])
        return self.result

        return self.result

    def postOrder(self):
        self.result = []
        cond = True
        S = []
        CN = 0
        while cond:
            while(CN!=(-1)):
                if(self.right[CN]!=(-1)):
                    S.append(self.right[CN])
                S.append(CN)
                CN = self.left[CN]
            CN = S.pop()
            if (len(S)>0):    
                if((self.right[CN]!=(-1))&(self.right[CN]==S[-1])):#might only need second condition
                    aux = S.pop()
                    S.append(CN)
                    CN = aux
                else:
                    self.result.append(self.key[CN])
                    CN = -1
            else:
                self.result.append(self.key[CN])
                CN = -1
            if(not S):
                cond=False
        return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


if __name__ == "__main__":
    main()
    
    