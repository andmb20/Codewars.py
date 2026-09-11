def well(x):
    alvo = 'good'
    if x.count(alvo) > 2:
        return 'I smell a series!'
    elif x.count(alvo) >= 1:
        return 'Publish!'
    else: return 'Fail!'

print(well(['bad', 'bad', 'bad']))# 'Fail!'
print(well(['good', 'bad', 'bad', 'bad', 'bad']))# 'Publish!'
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))# 'I smell a series!'