from MRE import Job
from locations import directory

input = directory('\Encuestas\input')
output = directory('\Encuestas\output')


def fmap(k1, v1, context):
  context.write(v1.capitalize(), 1)


def fred(k2, v2, context):
  n = 0
  for v in v2:
      n = n + 1
  context.write(k2, n)


Job(input, output, fmap, fred).waitForCompletion()
