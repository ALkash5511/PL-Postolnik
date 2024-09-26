import math
x = 17.421
y = 10.365*10**-3
z = 0.828*10**5
s = math.pow((y + math.pow((x-1), 1/3)), 1/4) / (math.fabs(x - y) * (math.sin(z)**2 + math.tan(z)))
print ("Ответ = {0:.6f}".format(s))