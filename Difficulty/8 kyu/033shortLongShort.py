def solution(a, b):
    return b + a + b if len(a) > len(b) else a + b + a

print(solution('45', '1'))# '1451'
print(solution('13', '200'))# '1320013'
print(solution('Soon', 'Me'))# 'MeSoonMe'
print(solution('U', 'False'))# 'UFalseU'