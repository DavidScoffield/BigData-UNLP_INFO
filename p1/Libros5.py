from MRE import Job
from locations import directory

input = directory('\Libros5\input')
output = directory('\Libros5\output')

# ------------ Obtener los títulos de todos los libros ------------
# def fmap(key, value, context):
#   if(value.isupper()):
#     print([key, value])
#     context.write(1, value)
  
# def fred(key, values, context):
#   for v in values:
#     context.write("TITULO ->",v)


# #  ------------ Obtener la cantidad de palabras promedio por párrafo ------------ 
# def fmap(key, value, context):
#   words = value.split()
#   length_words = len(words)
#   context.write(1, length_words)
  
# def fred(key, values, context):
#   total=0
#   quantity = 0
#   for v in values:
#     quantity += 1
#     total += v
#   context.write("PROMEDIO DE PALABRAS POR PARRAFO", total/quantity)



# ------------ Obtener la cantidad de párrafos promedio por libro ------------ 


# ------------ Obtener la cantidad de caracteres del párrafo más extenso ------------
# def fmap(key, value, context):
#   list_chars = list(value)
#   length_chars = len(list_chars)
#   context.write(1, length_chars)
  
# def fred(key, values, context):
#   max = 0
#   for v in values:
#     if( v > max):
#       max = v
#   context.write("CANTIDAD CARACTERES PARRAFO MAS EXTENSO", max)


# ------------ Cantidad total de párrafos con diálogos (se entiende por párrafo con diálogo  aquel que empieza con un guión) ------------ 
def fmap(key, value, context):
  if(value.startswith("-")):
    context.write(1, value)
  
def fred(key, values, context):
  c = 0
  for v in values:
    c += 1
  context.write("PARRAFOS CON DIALOGO", c)


# ------------ El diálogo más largo (se entiende por diálogo a una secuencia de párrafos con  diálogo que aparecen de manera consecutiva) ------------


# ------------ El top 20 de las palabras más usadas por cada libro ------------


Job(input, output, fmap, fred).waitForCompletion()