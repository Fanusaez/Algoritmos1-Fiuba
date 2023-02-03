#Escribir un programa que le pida una palabra al usuario, para luego imprimirla
#1000 veces, en una única línea, con espacios intermedios.
#Ayuda: Investigar acerca del parámetro end de la función print.

word = str(input('write any word: '))

for i in range(1000):
    print(word, end = ' ') 

 

