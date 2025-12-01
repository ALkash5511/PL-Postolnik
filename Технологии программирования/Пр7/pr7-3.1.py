a = int(input("a: "))
b = int(input("b: "))
mini = min(a, b)
maxi = max(a, b)
for i in range(mini, maxi+1):
    print(i, end=" ")
print()
for i in range(maxi, mini-1, -1):
    print(i)