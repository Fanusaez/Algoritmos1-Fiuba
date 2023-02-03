//Usando las funciones printf y sizeof, escribir un programa que imprima el
//tamaño en bytes de cada uno de los siguientes tipos: bool, char, short, int, long, float, double,
//bool*, char*, short*, int*, long*, float*, double*.


#include <stdio.h>
#include <stdbool.h>

int main() {   
    //int x = sizeof(bool);
    printf("El tamano de un bool es %lu\n", sizeof(bool));
    printf("El tamano de un char es %lu\n", sizeof(char));
    printf("El tamano de un short es %lu\n", sizeof(short));
    printf("El tamano de un int es %lu\n", sizeof(int));
    printf("El tamano de un long es %lu\n", sizeof(long));
    printf("El tamano de un float es %lu\n", sizeof(float));
    printf("El tamano de un double es %lu\n", sizeof(double));
    printf("El tamano de un bool* es %lu\n", sizeof(bool*));
    printf("El tamano de un char* es %lu\n", sizeof(char*));
    printf("El tamano de un short* es %lu\n", sizeof(short*));
    printf("El tamano de un int* es %lu\n", sizeof(int*));
    printf("El tamano de un long* es %lu\n", sizeof(long*));
    printf("El tamano de un float* es %lu\n", sizeof(float*));
    printf("El tamano de un double* es %lu\n", sizeof(double*));

    return 0;
}

