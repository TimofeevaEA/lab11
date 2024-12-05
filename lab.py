import math

def product(a, b):
    return a * b

#Тимофеева ЭА107б2

def quotient(a, b):
    if b == 0:
        return
    return a / b

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2


def sum_geometric_series(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)

def wordcount(text):
    return len(text.split())
#Тимофеева ЭА107б2

def findword(text,word):
    return word in text

def toupcase(text):
    return text.upper()
