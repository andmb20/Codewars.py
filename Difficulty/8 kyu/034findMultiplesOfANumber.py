def find_multiples(integer, limit):
    result = []
    for n in range(integer, limit + 1, integer):
        result.append(n)
    return result

print(find_multiples(5, 25))# [5, 10, 15, 20, 25]
print(find_multiples(1, 2))# [1, 2]