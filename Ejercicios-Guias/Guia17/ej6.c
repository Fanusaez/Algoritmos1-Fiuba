//Implementar la función void invertir(char *s) que invierte la cadena s (in-place).
#include <stdio.h>
#include <string.h>

void invertir(char *s) 
{
    int longitud = strlen(s);
    char aux;
    for (int izq = 0, der = longitud - 1; izq < (longitud/2); izq++, der--)
    {
        aux = s[izq];
        s[izq] = s[der];
        s[der] = aux;
    }
    printf("%s\n", s);
}

int main()
{   
    char s[30] = "hola como";
    invertir(s);
    return 0;
}

