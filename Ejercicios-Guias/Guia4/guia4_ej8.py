#Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños
#y el programa le debe decir a qué signo corresponde.

def signo_zodiaco():
    
    signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
    fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
    dia = int(input('ingrese dia de nacimiento: '))
    mes = int(input('ingrese mes de nacimiento: '))
    mes = mes - 1

    if dia > fechas[mes]:
        mes = mes + 1
    if mes == 12:
        mes = 0 

    return signo[mes]

print(signo_zodiaco())