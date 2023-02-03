//Escribir una función que permita calcular el área de un rectángulo dada su base
//y altura.

#include <stdio.h> 

int area_rectangulo(int base, int altura) {
    int area;
    area = base * altura;
    printf("El area es %d\n", area);
    return area;
}

main() { 
    int x;
    x = area_rectangulo(4,4);
    printf("el area xd xd %d\n",x);
}

