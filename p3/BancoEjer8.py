from datetime import datetime
from MRE import Job
from locations import directory

inputMovimientos = directory('\BancoEjer8\MovimientosBackup')
inputCajasDeAhorro = directory('\BancoEjer8\CajasDeAhorro')
outputTmp = directory('\BancoEjer8\outputTmp')
output = directory('\BancoEjer8\output')

# ----------------------
def fmapSavingBank(key, value, context):
  id_caja = key 
  id_client, balance = value.split("\t")
  context.write((id_caja, "C"), id_client)


def fmapFilterYearMonth(key, value, context):
  year_param = context["YEAR"]
  month_param = context["MONTH"]
  
  id_caja = key
  mount, datetime = value.split("\t")
  date, time = datetime.split(" ")
  year, month, day = date.split("-")
  
  if(int(year) == int(year_param) and int(month) == int(month_param)):
    context.write((id_caja, "MOV"), (mount, datetime))


def fShuffleCmp(key1, key2):
  if(key1[0] == key2[0]):
    return 0
  elif(key1[0] < key2[0]):
    return -1
  else:
    return 1


def fSortCmpFilterYearMonth(key1, key2):
  if(key1[1] == key2[1]):
    return 0
  elif(key1[1] == "C"):
    return -1
  else:
    return 1


def fredFilterYearMonth(key, values, context):
  id_client = None
  for v in values:
    if(id_client == None):
      id_client = v
    else:
      mov = v
      context.write(id_client, mov)

# ----------------------

def fmapSort(key, value, context):
  id_client = key
  mount, datetime_str = value.split("\t")
  context.write((id_client, datetime_str), (mount, datetime_str))


def fSortCmpSort(key1, key2):
  dt1 = datetime.strptime(key1[1], "%Y-%m-%d %H:%M:%S")
  dt2 = datetime.strptime(key2[1], "%Y-%m-%d %H:%M:%S")
  if(dt1 == dt2):
    return 0
  elif(dt1 < dt2):
    return -1
  else:
    return 1


def fredSort(key, values, context):
  id_client = key[0]
  
  for v in values:
    mount, datetime = v
    context.write(id_client, (mount, datetime))


# ----------------------


year = 2018
month = 1
window = 5
DATA = {"YEAR": year, "MONTH": month, "WINDOW": window}

# JOBs
jobFilterJoin = Job(inputMovimientos, outputTmp, fmapFilterYearMonth, fredFilterYearMonth)
jobFilterJoin.setParams(DATA)
jobFilterJoin.addInputPath(inputCajasDeAhorro, fmapSavingBank)
jobFilterJoin.setShuffleCmp(fShuffleCmp)
jobFilterJoin.setSortCmp(fSortCmpFilterYearMonth)
jobFilterJoin.waitForCompletion()


jobSort = Job(outputTmp, output, fmapSort, fredSort)
jobSort.setShuffleCmp(fShuffleCmp)
jobSort.setSortCmp(fSortCmpSort)
jobSort.waitForCompletion()


# Cantidad de subseries = len(movimientos) - window + 1
while True:
  pass