import math
x = 12.3*10**-1
y = 15.4
z = 0.252*10**3
s = math.pow(y, (x +1)) / (math.pow(math.fabs(y - 2), 1/3) + 3) + (x + y/2) * (math.pow(x + 1, -1 / math.sin(z))) / (2 * math.fabs(x + y))
print (" = {0:.4f}".format(s))