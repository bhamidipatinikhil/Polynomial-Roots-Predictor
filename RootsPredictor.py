import random

def slope(x):
    return 6*x**5 - 58*5*x**4 + 1338*4*x**3 - 15656*3*x**2 + 97493*2*x - 303198

def dd(x):
    return 30*x**4 - 58*5*4*x**3 + 1338*12*x**2 - 15656*6*x + 97493*2


ls = []

def max_gradient_ascent(x, alpha, iterations):
    initial_value = x
    for _ in range(iterations):
        x = x - (alpha*slope(x)/dd(x))
    ls.append(round(x, 5))

# n = max_gradient_ascent(n, 0.003, 10000)

for _ in range(30):
    a = 3
    b = 17

    n = random.randint(a, b)
    max_gradient_ascent(n, 0.03, (b-a)*100)

ls = [round(x, 5) for x in ls]

ls = set(ls)

print(list(ls))
# print(slope(1))