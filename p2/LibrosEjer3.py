from MRE import Job
from locations import directory

# Directorys
input = directory('\LibrosEjer3\input')
output = directory('\LibrosEjer3\output')
outputWordCount = directory('\LibrosEjer3\outputWordCount')
outputMinMaxProm = directory('\LibrosEjer3\outputMinMaxProm')


# MapReduce
def fmapWordCount(key, value, context):
  words = value.split()
  for w in words:
    context.write(w, 1)
    
def fredWordCount(key, values, context):
  c=0
  for v in values:
    c=c+v
  context.write(key, c)

def fmapMinMaxProm(key, value, context):
  context.write(1, (key, value))
  
def fredMinMaxProm(key, values, context):
  min = ["", float("inf")]
  max = ["", 0]
  total_amount = 0
  quantity = 0
  for v in values:
    key, valueString = v
    value = float(valueString)
    
    if(value < min[1]):
      min = [key, value]
    if(value > max[1]):
      max = [key, value]
    total_amount = total_amount + value
    quantity = quantity + 1
    
  context.write("MIN", min[0])
  context.write("MAX", max[0])
  context.write("PROM", total_amount/quantity)

def fmapStandarDesviation(key, value, context):
  prom = context["PROM"]
  context.write(1, (float(value) - float(prom))**2)

def fredStandarDesviation(key, values, context):  
  c = 0
  sum = 0
  for v in values:
    c += 1
    sum += v
  context.write("STANDAR_DESVIATION", (sum/(c-1)))

# JOB word count
jobWordCount = Job(input, outputWordCount, fmapWordCount, fredWordCount)
jobWordCount.setCombiner(fredWordCount)
jobWordCount.waitForCompletion()

# Job min, max, prom
jobMinMaxProm = Job(outputWordCount, outputMinMaxProm, fmapMinMaxProm, fredMinMaxProm)
jobMinMaxProm.waitForCompletion()


# Helper
with open(outputMinMaxProm + '\output.txt') as f:
  lines = f.readlines()
  PROM = {"PROM": lines[2].split("\t")[1]}

# Job standard desviation
jobFinal = Job(outputWordCount, output, fmapStandarDesviation, fredStandarDesviation)
jobFinal.setParams(PROM)
jobFinal.waitForCompletion()


# Final files JOIN 
data = data2 = ""

with open(outputMinMaxProm + '\output.txt') as fp:
	data = fp.read()

# Reading data from file2
with open(output + '\output.txt') as fp:
	data2 = fp.read()

data += data2

with open (output + '\output.txt', 'w') as fp:
	fp.write(data)
