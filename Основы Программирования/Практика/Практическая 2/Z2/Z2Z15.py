import math
x = 2.444
y = 0.869*10**-2
z = -0.13*10**3
s = (math.pow(x, y + 1) + math.exp(y-1)) * (1 + math.fabs(y - x)) / (1 + x * math.fabs(y - math.tan(z))) + (math.fabs(y - x)**2 / 2) - (math.fabs(y - x)**3 / 3)
print ("Ответ = {0:.6f}".format(s))