# a, b
# a * b
# a + b
# a - b

def f(a,b):
    result1 = a * b
    result2 = a + b
    result3 = a - b 
    return result1, result2, result3

a, b, c = f(2, 3)
print(a, b, c)