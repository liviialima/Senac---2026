import random

números = [91, 34, 67, 15, 82]
print("Lista original:", números)

números.sort(reverse=True)
print("Números sort():", números)

numeros3 = [6, 7, 8, 9, 10]

random.shuffles(numeros3)
print("Lista embaralhada:", numeros3)

numeros2 = [1,2,4,5,6,8]
numeros2.sort()
print("numeros2 sort():", numeros2)
