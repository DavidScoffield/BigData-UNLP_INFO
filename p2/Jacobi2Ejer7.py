from MRE import Job
from locations import directory

input = directory('\Jacobi2Ejer7\input')
output = directory('\Jacobi2Ejer7\output')


def fmap(key, value, context):
  name_var, value = value.split("\t")
  context.write(key, (name_var, value))


def fred(key, values, context):
  vars = context["incognitas"].copy()
  vars.insert(0,1)
  
  res = 0
  for name_var, value in values:
    if name_var.startswith("var"):
      index = int(name_var.replace("var", ""))
      res = res + (float(vars[index]) * float(value))
    else:
      # es TI
      res = res + float(value)
  context.write(key, res)


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



error = 0.0001
diff = 1
incognitas = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

while diff >= error:
  job = Job(input, output, fmap, fred)
  coefs = {"incognitas": incognitas}
  job.setParams(coefs)
  job.waitForCompletion()

  old_incog = incognitas.copy()
  incognitas = read_vars_ordered(output)

  diff = sum(list(map(lambda x, y: (x - y)**2, incognitas, old_incog)))

  print(diff)
  


