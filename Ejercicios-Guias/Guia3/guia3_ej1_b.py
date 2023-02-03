#La duración en horas, minutos y segundos de un intervalo dado en segundos.

def pase_seg_hms(segundos):
    h = segundos / 3600
    m = segundos / 60
    s = segundos 
    return h, m, s

#h, m, s = pase_seg_hms(4000000)

#print(h, m, s )

