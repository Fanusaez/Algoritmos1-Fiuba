
//Implementar una función que recibe un arreglo de números y su longitud y lo
//ordena mediante el algoritmo de ordenamiento por selección.

#include <stdio.h>

int encontrar_indice_maximo(int numeros[], int cantidad)
{
int indice_maximo = 0;
for(int i = 0; i < cantidad; i++)
    {
    if (numeros[i] > numeros[indice_maximo])
        {
        indice_maximo = i;
        }

    }
return indice_maximo;
}


void seleccion(int* numeros, int n) 
{

    for(int ordenados = 0; ordenados < n - 1; ordenados++)
    {   
        int indice_mayor = encontrar_indice_maximo(numeros, n - ordenados);
        int aux = numeros[n - ordenados -1];
        numeros[n - ordenados -1] = numeros[indice_mayor];
        numeros[indice_mayor] = aux;
    }
}

int main()
{
    int numeros[] = {1, 5, 3, 2, 6, 0};
    seleccion(numeros, 6);
    for(int i = 0; i < 6; i++)
    {   
        printf("%d\n", numeros[i]);
    }
    return 0;
}
