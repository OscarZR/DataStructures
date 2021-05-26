#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import namedtuple

Bracket = namedtuple("Bracket", ["caracter", "posicion"])


def coincidencia(izq, der):
    return (izq + der) in ["()", "[]", "{}"]


def inspeccion(texto):
    stack = []
    for i, next in enumerate(texto):
        if next in "([{":
            bracket = Bracket(next, i)
            stack.append(bracket)
        if next in ")]}":
            if not stack:
                return i + 1
            top = stack.pop()
            if (top.caracter == '(' and next != ')') or (top.caracter == '[' and next != ']') or (top.caracter == '{' and next != '}'):
                return i + 1
    if stack:
        return stack[0].posicion + 1
    return "Success"


def main():
    texto = input()
    coincide = inspeccion(texto)
    print(coincide)


if __name__ == "__main__":
    main()


# In[ ]:




