def square_or_square_root(arr: list[int]) -> list[int]:
    result= []
    for num in arr:
        if (num ** 0.5) % 1 == 0:
            result.append(int(num ** 0.5)) 
        else: result.append(num * num)

    return result

print(square_or_square_root([4, 3, 9, 7, 2, 1 ]))# [2, 9, 3, 49, 4, 1]
print(square_or_square_root([100, 101, 5, 5, 1, 1]))# [10, 10201, 25, 25, 1, 1]
print(square_or_square_root([1, 2, 3, 4, 5, 6]))# [1, 4, 9, 2, 25, 36]


#   def nearest_sq(n):
#       return round(n ** 0.5) ** 2

def nearest_sq(n: int) -> int:
    square: int = round(n ** 0.5)
    return square * square