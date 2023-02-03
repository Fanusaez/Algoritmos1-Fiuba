#Escribir una clase Caja para representar cuánto dinero hay en una caja de un
#negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
#de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
#5, 10, 20, 50, 100, 200, 500 y 1000 pesos.


class Caja:

    def __init__(self,caja):

        """ inicializa la clase caja y verifica que no haya billetes falsos"""
        billetes_validos =[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
        for billetes in caja:
            if billetes not in billetes_validos:
                raise ValueError("Denominación \"{}\" no permitida".format(billetes))
        self.caja = dict(caja)


    def __str__(self):
        total = 0
        for billete in self.caja:
            total += self.caja[billete] * billete
        return f"Caja {self.caja} total: {total} pesos"

    def agregar(self,otra_caja):
        """ agrega billetes a la caja"""
        billetes_validos =[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
        for billetes, cantidad in otra_caja.items():
            if billetes not in billetes_validos:
                raise ValueError("Denominación \"{}\" no permitida".format(billetes))
        for billetes,cantidad in otra_caja.items():
            if billetes in self.caja.keys():
                self.caja[billetes] += cantidad
            else:
                self.caja[billetes] = cantidad 
        return self.caja

    def quitar(self,otra_caja):
        """ saca billetes de una caja si estos son validos"""
        billetes_validos =[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
        for billetes in otra_caja:
            if billetes not in billetes_validos:
                raise ValueError("Denominación \"{}\" no permitida".format(billetes))
        validados = 0
        for billetes in otra_caja:
            if billetes in self.caja.keys() and self.caja[billetes] >= otra_caja[billetes]:

                validados += 1
        
            else:
                raise ValueError(f'No hay suficientes billetes de denominación \"{billetes}\"')

        if validados == len(otra_caja):
            for billetes in otra_caja:
                self.caja[billetes] -= otra_caja[billetes]
        
        lista_aux = []
        for billete in self.caja:
            if self.caja[billete] == 0:
                lista_aux.append(billete)
        for billete in lista_aux:
            del self.caja[billete]
        total= 0
        for billetes, cantidad in otra_caja.items():
            total+= billetes * cantidad
        return total
    
    