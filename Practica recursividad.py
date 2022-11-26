#Ejercicio 1

"""def factorial(n):
    if n == 0:
        return 0
    else:
        return n + factorial(n-1)
    
a = factorial(5)
print(a)"""

#Ejercicio 2

"""def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)
         
b = fibonacci(4)
print(b)"""

#Ejercicio 3

"""def imprime_cadena(Cad):
    if len(Cad) == 1:
        print(Cad[0])
    else:
        print(Cad[0])
        imprime_cadena(Cad[1:])

L = "Hola"
imprime_cadena(L)"""

#Ejercicio 4

"""def imprime_descendente(n):
    if n == 0:
        print(0)
    else:
        print(n)
        imprime_descendente(n-1)

imprime_descendente(8)"""

#Ejercicio 5

"""def imprime_ascendente(n, c=0):
        if c == n:
            print(c)
        else:
            print(c)
            imprime_ascendente(n,c+1)

imprime_ascendente(5)"""

#Ejercicio 6

"""def crear_lista(n,v):
  if n > 1:
    return [v] + crear_lista(n-1,v)
  return [v]
crear_lista(6,3)""" 

#Ejercicio 7

"""def suma_lista (l) :
    if len (l) == 1 :
        return l[0]
    return l[0] + suma_lista(l[1:])
l = [1,2,3]
print(suma_lista(l))"""

#Ejercicio 8

"""def encuentra_minimo(lista) :
    if len(lista) > 1 :
        a = lista [0]
        b = encuentra_minimo(lista[1:])
        if a < b :
            return a
        return b
    return lista [0]"""

#Ejercicio 9

"""def cadena_triangulo(a) :
    if a == 1 :
        return "*" 
    return cadena_triangulo(a-1) + "\n" + "*" * a

def main () :
    x = cadena_triangulo(5)
    print(x)
main()"""

#Ejercicio 10

"""def potencia (x,n) :
    if n == 0 :
        return 1 
    if n == 1 :
        return x
    else :
        m = potencia (x, n //2)
        resp = m * m
    if (n % 2 == 1) :
        resp =resp * x
    return resp

a = potencia (3,2)
print (a)"""

#Ejercicio 11

"""def invertir_cadena(cad):
    if len(cad) == 1:
        return cad[-1]
    else:
        return cad[-1] + invertir_cadena(cad[0:-1])
def main():
    z = "José"
    f = invertir_cadena(z)
    print(f)

main()"""

#Espiral 

"""def espiral(n,c = 0, j = 0, k = 1):
    mp = []
    if n  == k:
        return mp[c][j].append(k)
    else:
        return mp[c][j].append(k) + mp.append(espiral(n,c+1,j+1,k+1))
    
a = espiral(20)
print(a)
        """
        
n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))