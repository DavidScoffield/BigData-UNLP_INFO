from MRE import Job
from locations import directory

input = directory('\WordCount\input')
output = directory('\WordCount\output')

def fmap(key, value, context):
  words = value.split()
  for w in words:
    context.write(w, 1)

def fred(key, values, context):
  c=0
  for v in values:
    c=c+1
  context.write(key, c)

Job(input, output, fmap, fred).waitForCompletion()