import math
x = 1.825*10**2
y = 18.225
z = -3.298*10**-2
s = abs(math.pow(x, (y/x)) - math.pow((y/x), 1/3)) + (y - x) * (math.cos(y) - (z / (y - x))) / (1 + math.pow((y - x), 2))
print ("Ответ: {0:.5f}".format(s))
print (s)