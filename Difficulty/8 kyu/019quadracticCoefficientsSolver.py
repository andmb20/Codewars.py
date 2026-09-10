def quadratic(x1, x2):
    return(1, -(x1 + x2), +(x1 * x2)) 

# Best Approach: return (1,-x1-x2,x1*x2)


print(quadratic(0,1))# (1, -1, 0)
print(quadratic(4,9))# (1, -13, 36)
print(quadratic(2,6))# (1, -8, 12)
print(quadratic(-5,-4))# (1, 9, 20)

# Tenta fazer outro exemplo:

# x1 = 3, x2 = 5

# Expanda (x - 3)(x - 5) no papel.
# x² - 5x - 3x + 15 resultado = x² - 8x + 15