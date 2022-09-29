from MRE import Job
from locations import directory

input = directory('\WordCount4\input')
output = directory('\WordCount4\output')

def fmap(key, value, context):
  chars = list(value)
  for w in chars:
    context.write(w, 1)

def fred(key, values, context):
  c=0
  for v in values:
    c=c+1
  context.write(key, c)

Job(input, output, fmap, fred).waitForCompletion()