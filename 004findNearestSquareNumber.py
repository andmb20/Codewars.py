# Best Approach

#   def nearest_sq(n):
#       return round(n ** 0.5) ** 2

def nearest_sq(n: int) -> int:
    square: int = round(n ** 0.5)
    return square * square

print(nearest_sq(1))# 1
print(nearest_sq(2))# 1
print(nearest_sq(10))# 9
print(nearest_sq(111))# 121