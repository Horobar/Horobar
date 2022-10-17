a, b, c = 7, 3, 0
print(a, b, c)
c = a - b / 2 - a
print(a, b, c)
d = (3 * a + b) / (3.2 * 5 - 4.)
print(a, b, c, d)
c -= 2*c
print(a, b, c, d)
a = b = d * c
print(a, b, c, d)
d /= 2
print(a, b, c, d)
a = int(a)
print(a, b, c, d)
b = int(b/2)
print(a, b, c, d)
c *= c
print(a, b, c, d)
d += a + b + c
print(a, b, c, d)

print("f(x) = 2x^2 + 8")
print("f(100) = ", 2*(100**2) + 8)

print ("(2+4) / 3.0 == ", (2+4)/3)

print("Calculate the quare root of a=9")
a = 9
x1 = 1.
x2 = x1 - (x1**2 - a) / (2*x1)
x3 = x2 - (x2**2 - a) / (2*x2)
x4 = x3 - (x3**2 - a) / (2*x3)
x5 = x4 - (x4**2 - a) / (2*x4)
# runde auf 10^n Stellen
x = int(x5 * 1e1)/1e1 # auch:x = int(x5 * 10)/10
print("The square root of", a, "is (approx.): ", x)



