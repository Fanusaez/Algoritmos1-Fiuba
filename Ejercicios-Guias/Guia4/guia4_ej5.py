#Escribir funciones que resuelvan los siguientes problemas:
# a) Dado un año indicar si es bisiesto.
# b) Dado un mes y un año, devolver la cantidad de días correspondientes.
# c) Dada una fecha (día, mes, año), indicar si es válida o no.
# d) Dada una fecha, indicar los días que faltan hasta fin de mes.
# e) Dada una fecha, indicar los días que faltan hasta fin de año.
# f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
# g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido
#entre ambas, en años, meses y días.

def es_bisiesto(anio):
    if anio % 4 == 0 and anio % 100 ==0 and anio % 400 == 0:
        return True     
    if anio % 4 == 0 and anio % 100 != 0:
        return True   
    else:
        return False     

    return

#print(es_bisiesto(2020))
#print(es_bisiesto(1))


def es_fecha_corrrecta(dia, mes, anio):

    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    #comprobamos si es bisiesto, agregamos un dia a febrero
    if  es_bisiesto(anio):
        dias_mes[1] += 1
    # comprobamos que el mes sea valido
    if (mes < 1 or mes > 12):
        return False 
    #comprobamos dia valido
    mes -= 1
    if (dia <= 0 or dia > dias_mes[mes]):
        return False
    return True
    
#print(es_fecha_corrrecta(1, 3, 2))


def dias_restantes(dia,mes,anio):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if  es_bisiesto(anio):
        dias_mes[1] += 1
    if  not es_fecha_corrrecta(dia, mes, anio):
        return "fecha incorecta"
    dias_restantess = abs(dia - dias_mes[mes-1])

    return 'Los dias dias_restantess son: ' + str(dias_restantess)

print(dias_restantes(29, 2, 2020))






