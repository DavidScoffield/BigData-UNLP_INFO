from MRE import Job
from locations import directory

input = directory('\P1E1\input')
output = directory('\P1E1\output')

# Ejercicio A

# def fmap(k1, v1, context):
#     context.write(1, v1)

# def fred(k2, v2, context):
#     n = 0
#     for v in v2:
#       n = n + 1
#     context.write(k2, n)

# Ejercicio D

def fmap(k1, v1, context): 
  for v in range(int(v1)): 
    context.write(k1, v1) 

def fred(k2, v2, context): 
  n = 0 
  for v in v2: 
    n = n + 1 
  context.write(k2, n)


Job(input, output, fmap, fred).waitForCompletion()