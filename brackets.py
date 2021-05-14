# python3
#In this problem you will implement a feature for a text editor to find errors in the usage of brackets in the code.
'''
More formally, all brackets in the code should be divided into pairs of matching brackets, such that in
each pair the opening bracket goes before the closing bracket, and for any two pairs of brackets either
one of them is nested inside another one as in (foo[bar]) or they are separate as in f(a,b)-g[c].
The bracket [ corresponds to the bracket ], { corresponds to }, and ( corresponds to ).
'''
#El programa funciona entrando directamente a la función main(), dentro escribimos el String, posteriormente llamamos a la función que encuentra las desigualdades 'find_mismatch'
#nos regresará un valor booleano y una posición del arreglo. Dentro de la segunda función abrimos una lista para almacenar lo que encuentra, creamos dos tuplas con los valores de 
#abrir y cerrar paréntesis, corchetes o la otra. Creamos un directorio en donde se encuentra cada caracter de apertura con su correspondiente caracter de cerrada.
#Comienza el ciclo for, analizando el String que escribió el usuario, si encuentra un caracter de los mencionados, agrega a la lista el valor y su correspondiente cierre
#En caso de que lo encuentre cerrando, buscará si ya existe un abriendo en la lista creada para almacenar, si no se encuentra regresa False y el valor de la posición. 
#En caso contrario, analiza todo el resto del String y regresa True, imprimiendo Sucess 
#En el ultimo condicional, si el string está vacío igual cumple, por lo que no hay problema, en caso contrario, pues es Falso y manda la posición.

def find_mismatch(text):
    opening_brackets_stack = [] ; opened=tuple('([{') ; closed=tuple(')]}')
    map=dict(zip(opened,closed))
    for i, next in enumerate(text):
        if next in opened:
            opening_brackets_stack.append(map[next])
        elif next in closed:
            if not opening_brackets_stack or next!= opening_brackets_stack.pop():
                return False,i
    if not opening_brackets_stack:
        return True,0
    else:
        return False,i

def main():
    text = input()
    mismatch,num = find_mismatch(text)
    if mismatch == True:
        print('Success')
    else:
        print(num+1)
main()


'''
import sys


class Bracket:
#     It stores a bracket type which is one of [, (, { and position of the bracket

    def __init__(self, bracket, position):
        self.bracket = bracket
        self.position = position

    def match(self, char):
        """Matches given character with the bracket's type."""

        if self.bracket == '[' and char == ']':
            return True
        if self.bracket == '{' and char == '}':
            return True
        if self.bracket == '(' and char == ')':
            return True
        return False


def checker(text):
    stack = []
    for index, char in enumerate(text, start=1):

        if char in ("[", "(", "{"):
            stack.append(Bracket(char, index))

        elif char in ("]", ")", "}"):
            if not stack:
                return index

            top = stack.pop()
            if not top.match(char):
                return index
    if stack:
        top = stack.pop()
        return top.position

    return "Success"


if __name__ == "__main__":
    text = sys.stdin.readline()
    print(checker(text))
'''