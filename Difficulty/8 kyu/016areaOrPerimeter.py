# Best Approach
# def area_or_perimeter(l, w):
#     return l * w if l == w else (l + w) * 2

def area_or_perimeter(l , w):
    return l * w if(l == w) else l + l + w + w  


print(area_or_perimeter(4, 4))#  16)
print(area_or_perimeter(6, 10))#  32)