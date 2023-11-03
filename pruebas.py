string = "-Cuando el Duque de Ayamonte me nombró bibliotecario y archivero de su ilustre casa, creí que mi vida iba a deslizarse tranquilamente en los bajos de su palacio de Madrid; y hasta ví en lontananza la publicación de varios trabajos de índole histórica, que desde hacía muchos años codiciaba, y los cuales, sin embargo, permanecen inéditos, su mayor parte todavía dentro de mi tintero. Todo lo contrario de lo que yo esperaba, el magnate resultó ser un investigador incansable, y mientras él dedicaba largas horas a explorar en los archivos de la Corte, me enviaba a menudo en busca de documentos a Provincias."

def split_letters(string):
    return list(string)
  
  
print(len(split_letters(string)))
# for i in split_letters(string):
#     print(i)

print(string.startswith("-"))

print(2 < float("-inf"))

from datetime import datetime 

# year="2019"
# month="9"
# day="15"
# date = date(int(year), int(month), int(day))


# today = date.today()

date = datetime.strptime("2018-01-29 04:41:18", "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime("2018-01-13 12:36:56", "%Y-%m-%d %H:%M:%S")

print(date > date2)
