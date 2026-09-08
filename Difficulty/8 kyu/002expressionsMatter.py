#   Best Approach

#   def expression_matter(a, b, c):
#       return max(a*b*c, a+b+c, (a+b)*c, a*(b+c)) 

def expression_matter(a, b, c):
    exp1 = a + b + c
    exp2 = a * b * c
    exp3 = a * b + c
    exp4 = a + b * c
    exp5 = a * (b + c)
    exp6 = (a + b) * c
    resultado = [exp1, exp2, exp3, exp4, exp5, exp6]
    return max(resultado)

print(expression_matter(2, 1, 2)) #6
print(expression_matter(2, 1, 1)) #4
print(expression_matter(2, 2, 4)) #16
print(expression_matter(3, 3, 3)) #27
print(expression_matter(1, 1, 1)) #3
print(expression_matter(1, 2, 3)) #9
print(expression_matter(1, 3, 1)) #5
print(expression_matter(2, 2, 2)) #8
print(expression_matter(5, 1, 3)) #20