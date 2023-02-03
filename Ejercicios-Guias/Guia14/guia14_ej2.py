#Escribir las clases Impresora y Oficina que permita modelar el funcionamiento
#de un conjunto de impresoras conectadas en red.

from clases import *

class Oficina:
    '''
    DOC: Completar
    ''' 
    
    def __init__(self):
        self.impresoras_oficina = {}        
    
    def agregar_impresora(self, impresora):
        self.impresoras_oficina[impresora.nombre] = impresora
        
    def impresora(self, nombre):
       return self.impresoras_oficina[nombre] 

    def quitar_impresora(self, nombre):
        self.impresoras_oficina[nombre] = None

    def obtener_impresora_libre(self):
        minimo = 100
        impresora = ""
        for _ , valor in self.impresoras_oficina.items():
            if valor.documentos < minimo:
                minimo = valor.documentos
                impresora = valor
        return impresora    
    

class Impresora:
    '''
    DOC: Completar
    '''

    def __init__(self, nombre, cantidad):
        self.nombre = nombre    
        self.tinta = cantidad
        self.capacidad = cantidad
        self.cola = Cola()
        self.documentos = 0
    
    
    def encolar(self, documento):
        
        self.cola.encolar(documento)
        self.documentos += 1

    def imprimir(self):
        
        if self.cola.esta_vacia():
            print("No tengo documentos para imprimir")
        elif self.tinta < 1:
            print("No tengo tinta")
        else:
            print(f"{self.cola.desencolar()} impreso")
            self.tinta -= 1
            self.documentos -= 1
           

    def cargar_tinta(self):
        self.tinta = self.capacidad

o = Oficina()
o.agregar_impresora(Impresora('HP1234', 1))
o.agregar_impresora(Impresora('EPSON666', 5))
o.impresora('HP1234').encolar('tp1.pdf')
o.impresora('EPSON666').encolar('tp2.pdf')
o.impresora('HP1234').encolar('tp3.pdf')
o.obtener_impresora_libre().encolar('tp4.pdf')
o.impresora('HP1234').imprimir()
o.impresora('HP1234').imprimir()
o.impresora('HP1234').cargar_tinta()
o.impresora('HP1234').imprimir()
o.impresora('HP1234').imprimir()
o.impresora('EPSON666').imprimir()
o.impresora('EPSON666').imprimir()
o.impresora('EPSON666').imprimir()
