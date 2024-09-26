import math
x = -2.235*10**-2
y = 2.23
z = 15.221
s = math.exp(math.fabs(x - y)) * (math.pow((math.fabs(x - y)), (x + y))) / (math.atan(x) + math.atan(z)) + math.pow((x**6 + math.pow(math.log(y), 2)), 1/3)
print ("Ответ: = {0:.4f}".format(s))