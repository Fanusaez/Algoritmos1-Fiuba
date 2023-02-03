//Escribir una función que reciba un número entero n y calcule el factorial de n. 
//La función se puede escribir estar en forma iterativa o recursiva.

#include <stdio.h>

int factorial(int n) {
    int i, factorial = 1;
    for (i = 1; i <= n; i++) {
       factorial *= i;
    }
    printf("el factorial de %d es %d: \n", n, factorial);
    return factorial;
}

int main() {
    printf("%i\n", factorial(5));
    return 0;
}