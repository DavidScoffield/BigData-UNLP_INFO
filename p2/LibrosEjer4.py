from MRE import Job
from locations import directory

# Directorys
input = directory('\LibrosEjer4\input')
output = directory('\LibrosEjer4\output')
outputProm = directory('\LibrosEjer4\outputProm')


# MapReduce
def fmapProm(key, value, context):
  words = value.split()
  context.write(1, (value, len(words)))
    
def fredProm(key, values, context):
  quantity_paragraphs = 0
  total_words = 0
  for v in values:
    total_words += v[1]
    quantity_paragraphs += 1
  context.write("PROM", total_words/quantity_paragraphs)

def fmapMajorThanProm(key, value, context):
  prom = context["PROM"]
  words = value.split()
  if(len(words) > float(prom)):
    context.write(1, value)
    
def fredMajorThanProm(key, values, context):
  for v in values:
    context.write("MAJOR_THAN_PROM", v)

# JOB Prom
jobProm = Job(input, outputProm, fmapProm, fredProm)
jobProm.waitForCompletion()

# Helper
with open(outputProm + '\output.txt') as f:
  lines = f.readlines()
  PROM = {"PROM": lines[0].split("\t")[1]}

jobMajorThenProm = Job(input, output, fmapMajorThanProm, fredMajorThanProm)
jobMajorThenProm.setParams(PROM)
jobMajorThenProm.waitForCompletion()


