from heapq import merge
from MRE import Job
from locations import directory
from datetime import date

input = directory('\Inversionistas\input')
output = directory('\Inversionistas\output')

def calculate_age(born):
  today = date.today()
  return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def fmap(k1, v1, context):
  name, day, month, year, amount = v1.split('\t')

  born = date(int(year), int(month), int(day))
  
  context.write("YOUNG_NAME", (name, born))
  context.write("TOTAL_AMOUNT", int(amount))
  context.write("AGE", calculate_age(born))


def fred(k2, v2, context):
  more_young = 0
  total_amount = 0
  quantity_persons = 0
  total_age = 0
  for v in v2:
    if(k2 == "YOUNG_NAME"):
      if(more_young == 0):
        more_young = v
      else: 
        if(more_young[1] < v[1]):
          more_young = v
    elif(k2 == "TOTAL_AMOUNT"):
      total_amount = total_amount + v
    elif(k2 == "AGE"):
      quantity_persons = quantity_persons + 1
      total_age = total_age + v

  if(k2 == "YOUNG_NAME"):
    context.write("YOUNG_NAME", more_young)
  elif(k2 == "TOTAL_AMOUNT"):
    context.write("TOTAL_AMOUNT", total_amount)
  elif(k2 == "AGE"):
    context.write("AVR_AGE", total_age/quantity_persons)


Job(input, output, fmap, fred).waitForCompletion()
