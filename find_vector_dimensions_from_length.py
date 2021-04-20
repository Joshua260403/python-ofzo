from math import isclose, sqrt

l = 60

for i in range(1,l):
    n = sqrt((l**2) - (i**2))
    if isclose(n, int(n)):
        print(i, n)
print("done")
