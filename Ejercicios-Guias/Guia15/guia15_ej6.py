"""
Escribir una función recursiva que calcule recursivamente el n-ésimo número
triangular (el número 1 + 2 + 3 + ⋯ + n).
"""

def numero_triangular(n):

    if n == 1:
        return 1
    return numero_triangular(n-1) + n

print(numero_triangular(6))