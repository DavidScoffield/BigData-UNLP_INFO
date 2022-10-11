from MRE import Job
from locations import directory

input = directory('\WebsiteEjer4\input')
output = directory('\WebsiteEjer4\output')
outputLength = directory('\WebsiteEjer4\outputLength')

def fmapLength(key, value, context):
  id_page, time = value.split("\t")

  context.write(1, time)

def fredLength(key, values, context):
  c = 0
  for v in values:
    c += 1
  context.write("LENGTH", c)
  
def fmapMediana(key, value, context):
  id_page, time = value.split("\t")
  
  context.write((1, time), time)
  
def fredMediana(key, values, context):
  length = context["LENGTH"]
  index_medio = int((int(length) / 2) + 1)
  value = -1

  c = 0
  for v in values:
    print(v)
    c += 1
    if c == index_medio:
      value = v
      break 
  context.write("MEDIANA", value )

def fShuffleCmp(key1, key2):
  if(key1[0] == key2[0]):
    return 0
  elif(key1[0] < key2[0]):
    return -1
  else:
    return 1


def fSortCmp(key1, key2):
  if(int(key1[1]) == int(key2[1])):
    return 0
  elif(int(key1[1]) < int(key2[1])):
    return -1
  else:
    return 1



jobLenght = Job(input, outputLength, fmapLength, fredLength)
jobLenght.waitForCompletion()

# Helper
with open(outputLength + '\output.txt') as f:
  lines = f.readlines()
  LENGTH = {"LENGTH": lines[0].split("\t")[1]}
  
jobMediana = Job(input, output, fmapMediana, fredMediana)
jobMediana.setParams(LENGTH)
jobMediana.setShuffleCmp(fShuffleCmp)
jobMediana.setSortCmp(fSortCmp)
jobMediana.waitForCompletion()
