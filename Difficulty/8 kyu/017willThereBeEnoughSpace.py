def enough(cap, on, wait):
    return on + wait - cap if cap - on - wait <= 0 else 0

print(enough(10, 5, 5))# 0
print(enough(100, 60, 50))# 10
print(enough(20, 5, 5))# 0