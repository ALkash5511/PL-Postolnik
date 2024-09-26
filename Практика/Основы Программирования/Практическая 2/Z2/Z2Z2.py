import math
x = -4.5
y = 0.75*10**-4
z = -0.845*10**2
s = math.pow((9 + math.pow((x -y), 2)), 1/3) / (x**2 + y**2 + 2) - math.exp(math.fabs(x-y)) * math.tan(z)**3
print ("s = {0:.5f}".format (s))