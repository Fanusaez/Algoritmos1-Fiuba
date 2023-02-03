/*
Implementar una función que reciba un mensaje y dos números enteros min y
max. La función debe pedir al usuario que ingrese un número entero entre min y max (inclusive)
y devolverlo. Si el usuario ingresa un valor inválido se le debe informar y pedir que ingrese un
nuevo valor, repitiendo hasta que ingrese un número válido.
*/

# include <stdio.h> 

int pedir_entero(int min, int max, char mensaje[]) {
    int n;
    printf("%s [%i..%i]\n", mensaje, min, max);
    printf("Por favor ingresa un numero entre %i y %i\n", min, max);
    scanf("%i\n, &n);
    while (n > max) {
        printf("Por favor ingresa un numero entre %i y %i\n", min, max);
        scanf("%i\n", &n);
    }
    return n;
}

int main(){
    return pedir_entero(4, 40, "decime tu num");
}