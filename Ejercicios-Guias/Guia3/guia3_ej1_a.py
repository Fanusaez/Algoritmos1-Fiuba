#Escribir dos funciones que permitan calcular:
#la duración en segundos de un intervalo dado en horas, minutos y segundos
    
def calculo(horas, minutos, segundos):
    h = horas * 3600
    m = minutos * 60
    s = segundos    
    return h, m, s

h, m, s = calculo(30, 80, 890)
print(h, m, s)