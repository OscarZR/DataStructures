# python3
'''
Este programa funciona mejor usando recursividad, pero utilizando el método visto en clase, en el cual, al acomodar una lista podemos seccionarla en dos partes , y enlazar un
nodo raíz el cual funcionara como estilo de pivote. Posteriormente, recorreremos los nuevos subárboles de atrás hacia adelante. De esta manera, ahorramos mucho tiempo.
La implementación consta de la creación de una clase, la cual apenas llamarla, se crean dos arreglos, el primero, llamado cambios nos ayudará a almacenar los cambios realizados
en forma de tuplas, el segundo almacena la información introducida.
Luego, al llamar la función llamadas, llama a lectura, donde introduce datos, luego a la función Generación, en donde se particiona el arreglo y se recorre a la inversa, dentro
del ciclo se hace llamado a la función de recorrido, en el cual se hacen las comparaciones: ¿cómo? ah pues bein fácil. Al llamar a recorrido, pasamos el índice del ciclo for de 
la función Generación, luego aquí está la magia, si el doble de dicho indice más uno(idea obtenida por el quiz) es menor que la longitud del arreglo, r y l toman ese mismo valor
si resulta que ya es muy grande, se bota del ciclo. Va checando con los elementos de dichos índices, hasta que r o l tomen el valor del índice menor. Por lo que si se llego a 
modificar, se almacena el indice del ciclo for de la función anterior y el nuevo índice encontrado, en TUPLAS, posteriormente se hace recursividad hasta que ahora sí sobrepase 
el doble de n+ 1. =)
'''
class Heap:
    def __init__(self):
        self._cambios=[] ; self._info=[]
    def Lectura(self):
        n=int(input()) ; self._info=[int(i) for i in input().split()]
        if n!=len(self._info):
            print('no same lenght')
        else:
            pass
    def Imprimir(self):
        print(len(self._cambios))
        for cambio in self._cambios:
            print(cambio[0],cambio[1])
    def recorrido(self,i):
        n = len(self._info) ; indice_menor = i
        '''
        if (2*i+1)<n:
            l = 2*i+1 ; r=2*i+1
        else:
            r=-1 ; l=-1
        '''
        l = 2*i+1 if (2*i+1<n) else -1 
        r = 2*i+2 if (2*i+2<n) else -1 
#         print(i,l,r)
        if l != -1 and self._info[l] < self._info[indice_menor]:
            indice_menor= l
        if r != - 1 and self._info[r] < self._info[indice_menor]:
            indice_menor = r
        if i != indice_menor:
            self._cambios.append((i, indice_menor))
            self._info[i], self._info[indice_menor] = self._info[indice_menor], self._info[i]
            self.recorrido(indice_menor)
    def Generacion(self):
        for j in range(len(self._info)//2,-1,-1):
            #print(j)
            self.recorrido(j)

    def llamadas(self):
        self.Lectura()
        self.Generacion()
        self.Imprimir()
if __name__=='__main__':
    hb=Heap()
    hb.llamadas()
    

'''
def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
'''