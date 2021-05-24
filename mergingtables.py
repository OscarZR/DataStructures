# python3

'''
Este programa está bien chido, verda de Dios.
1) Comienza con el llamado a main(), desde donde se piden los datos, se asegura de la longitud del arreglo, Después creo el objeto Alan el cual manda a la clase el  numero de tablas
y el arreglo del numero de columnas de cada tabla. Con esto, se crean distintos arreglos:
> Arreglo counts: lo inicio con un ceero y se le agregan los valores que están dentro del arreglo que introduce el usuario.
> Arreglo rango: es un arreglo de cero con la longitus de counts.
> Arreglo padre: Una lista de enteros desde el cero hasta n.
Y también se crean dos valores, uno es n que introduce el usuario. y el otro es el número máximo de filas que tenga algún archivo.
2) De nuevo, en la función main(), se inicializa un ciclo for para que introduzcamos el archivo fuente y el archivo destino. Y esos se los pasamos a Uniones, dentro de la clase.
3) En Uniones(merge), pasamos el valor del archivo fuente y del archivo destino a la función regresaPadre, el cúal nos regresará un entero.
4) En RegresaPadre, se crea un arreglo vacío, y se usa el valor raíz. Ahora, mientras el valor raíz sea distinto al valor del arreglo padre en la posición raíz se agrega el valor
del arreglo en la lista auxiliar. Y después se igualan el valor de la raíz con ese valor. Esto sólo nos va a ayudar para saber la ubicación del archivo. Ahora, para cada valor 
dentro del auxiliar, es decir, un entero, buscaremos dentro del arreglo de padre cado archivo con valor de auxiliar y lo igualaremos al valor de raíz. Luego, este valor es el
que se regresa. Básicamente, sabremos qué filas se han agregado a dichos archivos. Es decir, guardamos el puntero.
5) Lo anterior funcionará para obtener el puntero. Ahora, si resulta que ambas raíces son iguales, nos retachamos. Es decir, imprimimos el valor máximo de filas que ya existia.
Ahora que si el valor dentro del arreglo de rango entre las dos raíces es mayor o IGUAL (lo que casi siempre sucede) el valor del arreglo padre en la posición de raiz fuente
es igual al valor de la raíz destino (como se esperaba). Ora si no se cumple lo anterior, pues hacemos lo contrario, el valor de la raíz destino será igual al valor de la raíz fuente.
Y ahora sí agregariamos un valor al arreglo de rangos.
6) Una vez que terminan las comparaciones, sumamos el valor de las filas del archivo fuente al archivo destino. Y el valor dentro del arreglo original de la raíz fuente se hace cero
Esto es porque le agregamos sus filas al nuevo archivo, pero el puntero se guardó ya en el arreglo padre. Por lo que si quisieramos sumarle las filas de uno de los archivos a ellos
ya no tiene más filas que dar. Cómo funciona con los enlaces de Química.
7) Finalmente se compara el máximo anterior y el que se acaba de formular. Si es mayor pues se actualiza, a poco no?
8) Se imprime el mayor número de filas de todos los archivos existentes.
--------------o-----------------------o-----------------------------------------o-------------------------------------o-----------------------------------o------------------------o
class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        return True

    def get_parent(self, table):
        # find parent and compress path
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
------------------o------------------------------------o-------------------------------------o---------------------------------------o----------------------o------------------o
'''

import sys

class Database(object):
    def __init__(self,n,counts):
        self.n=n ; self.counts=[0] + counts ; self.rango=[0]*(n+1)
        self.padre=list(range(0,n+1)) ; self.maximus=max(self.counts)
        #print(self.rango,'\n',self.padre,'\n',self.maximus,'\n',self.n)
    def PadreRegresa(self,num):
        aux=[] ; raiz=num
        while raiz!= self.padre[raiz]:
            aux.append(self.padre[raiz])
            raiz=self.padre[raiz]
        for j in aux:
            self.padre[j]=raiz
        #print(aux)
        return raiz
    def Uniones(self,destino,fuente):
        raiz_fuente = self.PadreRegresa(fuente)
        #print(self.padre)
        raiz_destino= self.PadreRegresa(destino)
        #print(self.padre,'\n',self.rango)
        if raiz_fuente == raiz_destino:
            return
        if self.rango[raiz_fuente] >= self.rango[raiz_destino]:
            self.padre[raiz_fuente]=raiz_destino
        else:
            self.padre[raiz_destino] = raiz_fuente
            if self.rango[raiz_fuente] == self.rango[raiz_destino]:
                self.rango[raiz_fuente] +=1
        self.counts[raiz_destino] += self.counts[raiz_fuente]
        self.counts[raiz_fuente] = 0

        if self.maximus < self.counts[raiz_destino]:
            self.maximus = self.counts[raiz_destino]

    def ObtenerMaximus(self):
        return self.maximus

def main():
    n,m=map(int,sys.stdin.readline().split())
    counts = list(map(int, sys.stdin.readline().split()))
    assert len(counts) == n
    Alan=Database(n,counts)
    for i in range(m):
        destino, fuente = map(int, sys.stdin.readline().split())
        Alan.Uniones(destino, fuente)
        print(Alan.ObtenerMaximus())

if __name__=='__main__':
    main() 