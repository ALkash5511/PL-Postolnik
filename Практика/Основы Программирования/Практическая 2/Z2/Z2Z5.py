import math
x = -15.246
y = 4.642*10**-2
z = 21
s = math.log(math.pow(y, (-math.sqrt(math.fabs(x))))) * (x - y/2) + math.pow(math.sin(math.atan(z)), 2)
print ("Ответ: = {0:.3f}".format(s))