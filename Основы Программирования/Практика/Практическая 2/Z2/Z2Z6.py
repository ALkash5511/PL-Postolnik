import math
x = 16.55*10**-3
y = -2.75
z = 0.15
s = math.sqrt(10*(math.pow(x, 1/3) + math.pow(x, (y+2)))) * (math.pow(math.asin(z), 2) - math.fabs(x - y))
print ("Ответ: = {0:.4f}".format(s))