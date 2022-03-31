# Question 1
def power(b, n):
    if n == 0:
        return 1
    else:
        return b * power(b, n - 1)

# Question 2
def double(n):
     if n == 0:
          return 1
     else:
          return double(n - 1) * 2
print(double(3))

# Question 3
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(15, 9))
print(gcd(13, 8))


# Question 4
def m(a, b):
   if a < b:
     return a
   else:
     return m(a - b, b)

print(m(3, 5))
print(m(7, 5))
print(m(14, 5))
print(m(37, 7))
print(m(54, 11))