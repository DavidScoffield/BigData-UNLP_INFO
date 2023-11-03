from pyspark import SparkContext
sc = SparkContext("local", "MyProgram")

clientes = sc.textFile("./banco/Clientes/Clientes.txt")

print(clientes.take(5))