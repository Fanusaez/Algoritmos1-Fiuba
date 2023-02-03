//Escribir una función que reciba un arreglo de números y la cantidad de elementos, 
//y devuelva el promedio.

#import <stdio.h>
float promedio(float numeros[], int n){
    int i;
    float suma_notas = 0; float promedio = 0;
    for (i = 1; i < n; i++){
        suma_notas += numeros[i];
    }
    promedio = suma_notas / n;
    return promedio;
}
int main(){
    float numeros[6] = {1.0,4.0,5.0,6.0,3.0,6.0};
    printf("El promedio es: %f\n", promedio(numeros, 6));
    return 0;
}

