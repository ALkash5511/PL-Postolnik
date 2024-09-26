import math
x = 6.251
y = 0.827
z = 25.001
s = math.pow(y, math.pow(math.fabs(x), (1/3))) + math.pow(math.cos(y), 3) * math.fabs(x - y) * (1 + math.pow(math.sin(z), 2) / math.sqrt(x + y)) / (math.exp(math.fabs(x - y)) + x/2)
print ("Ответ = {0:.6f}".format(s))