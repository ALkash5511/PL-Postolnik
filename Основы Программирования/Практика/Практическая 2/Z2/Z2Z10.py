import math
x = 3.981*10**-2
y = -1.625*10**3
z = 0.512
s = 2**-x * math.sqrt(x + math.pow(math.fabs(y), 1/4)) * math.pow(math.exp(x - 1/math.sin(z)), 1/3)
print ("Ответы = {0:.5f}".format(s))