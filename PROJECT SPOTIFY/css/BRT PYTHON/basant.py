def bpower(a, n):
 pow = 1
 for i in range(n):
    pow = pow * a
 return pow
# Divide and Conquer method
#The problem can be recursively defined by:
# dpower(x, n) = dpower(x, n / 2) * dpower(x, n / 2); // if n is even
# dpower(x, n) = x * dpower(x, n / 2) * dpower(x, n / 2); // if n is odd
def dpower(x, y):
 if (y == 0):
    return 1
 elif (int(y % 2) == 0):
    return (dpower(x, int(y / 2)) *
 dpower(x, int(y / 2)))
 else:
    return (x * dpower(x, int(y / 2)) *
 dpower(x, int(y / 2)))
# Main block
a=int(input("Enter a :"))
n=int(input("Enter n :"))
print("Brute Force method a^n : ",bpower(a,n))
print("Divide and Conquer a^n : ",dpower(a,n))
