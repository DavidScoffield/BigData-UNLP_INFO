from MRE import Job
from locations import directory

input = directory('\Jacobi2Ejer5\input')
output = directory('\Jacobi2Ejer5\output')
initialVars = directory('\Jacobi2Ejer5\initialVars')

def fShuffleCmp(key1, key2):
  if(key1[1] == key2[1]):
    return 0
  elif(key1[1] < key2[1]):
    return -1
  else:
    return 1


def fSortCmp(key1, key2):
  if(int(key1[0]) == int(key2[0])):
    return 0
  elif(int(key1[0]) < int(key2[0])):
    return -1
  else:
    return 1


def fmap(key, value, context):
  name_var, value = value.split("\t")
  context.write(("1", key), (name_var, value))
  
  
def fmapVars(key, value, context):
  # Deberia saber de antemano el lenght del archivo vars
  for i in range(1, 16):
    name_var = "var" + str(i)
    context.write(("0", name_var), (key, value))


def fred(key, values, context):
  vars = {}
  vars["TI"] = 1

  paso = 0
  res = 0
  for name_var, value in values:
    if(paso < 15):
      vars[name_var] = value
      paso += 1
    else:
      res = res + (float(vars[name_var]) * float(value))

  context.write(key[1], res)
  

# Utils
def read_vars_ordered(directory):    
  list_tmp = []
  with open(directory + "\output.txt", 'r') as f:
    for line in f:
      key, value = line.split("\t")
      key = int(key.replace("var", ""))
      value = float(value.replace("\n", ""))
      list_tmp.append([key, value])
    
  list_tmp.sort(key=lambda x: x[0])
  return list(map(lambda x: x[1], list_tmp))


def createJob(input, output, fmap, fred, fSortCmp, fShuffleCmp):
  job = Job(input, output, fmap, fred)
  
  if(fSortCmp != None):
    job.setSortCmp(fSortCmp)

  if (fShuffleCmp != None):
    job.setShuffleCmp(fShuffleCmp)

  return job



# JOBs
job = createJob(input, output, fmap, fred, fSortCmp, fShuffleCmp)
job.addInputPath(initialVars, fmapVars)
job.waitForCompletion()


error = 0.0001
diff = 1
incognitas = read_vars_ordered(initialVars)

while diff >= error:
  job = createJob(input, output, fmap, fred, fSortCmp, fShuffleCmp)
  job.addInputPath(output, fmapVars)
  job.waitForCompletion()
  
  old_incog = incognitas.copy()
  incognitas = read_vars_ordered(output)

  diff = sum(list(map(lambda x, y: (x - y)**2, incognitas, old_incog)))

  print(diff)
  


