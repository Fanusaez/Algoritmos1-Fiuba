# Agenda simplificada
#Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo,
#telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo
#la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos).
#Debe devolver una lista con todas las tuplas encontradas.

def agenda_simlificada(busqueda, contactos):
    """
    Recibe una cadena a buscar y una agenda en forma de lista de tuplas que continenen
    el nombre y el telefono del contacto.
    """
    lista_rta = []
    for i in range(len(contactos)):
        if busqueda in contactos[i][0].lower():
            lista_rta.append(contactos[i])
    return lista_rta

print(agenda_simlificada('Juani', [('Juani K', 99998888), ('Alejo Mora', 144444445)]))
 #  no pude
