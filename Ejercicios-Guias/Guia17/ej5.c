//Implementar la función unsigned int strlen(const char *s) que devuelve la
//longitud de la cadena s (sin contar el último caracter '\0'). 
//La función se puede escribir estar en forma iterativa o recursiva.

#include <stdio.h>

unsigned int strlen(const char *s) 
{
    int longitud = 0;
    while (s[longitud] != '\0') // tener cuidado '' != ""
    {
        longitud += 1;
    }
    return longitud;

}

int main(){
    char cadena[30] = "Hola como estas baby";
    printf("la longitud de la cadena es: %d\n", strlen(cadena));
    return 0;
}

