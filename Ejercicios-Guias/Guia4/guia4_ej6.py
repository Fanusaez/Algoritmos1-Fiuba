# Suponiendo que el primer día del año fue lunes, escribir una función que reciba
#un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca
#Por ejemplo: si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'.


def dia_semana(dia):
    resto = dia % 7 
    nombre_dia = ""
    if resto == 1:
        nombre_dia = "lunes"
    if resto == 2:
        nombre_dia == "martes"
    if resto ==3:
        nombre_dia = "miercoles"
    if resto == 4:
        nombre_dia = "jueves"
    if resto == 5:
        nombre_dia = "viernes"
    if resto == 6:
        nombre_dia = "sabado"
    else:
        nombre_dia = "domindo"
    return nombre_dia

print(dia_semana(23))