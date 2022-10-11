from MRE import Job
from locations import directory

input = directory('\JacobiVarsEjer6\input')
output = directory('\JacobiVarsEjer6\output')

def fmap(key, value, context):
  for i in range(1, int(value)+1):
    context.write(i, i)

def fred(key, values, context):
  for v in values:
    pass
  name_var = "var" + str(key)
  context.write(name_var, key)
  


job = Job(input, output, fmap, fred)
job.waitForCompletion()
