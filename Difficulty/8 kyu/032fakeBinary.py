def fake_bin(x):
    fakeBinValue = ''
    for n in x:
        if int(n) >= 5:
            fakeBinValue += '1'
        else: fakeBinValue += '0'
    return fakeBinValue

print(fake_bin("45385593107843568"))# "01011110001100111"
print(fake_bin("509321967506747"))# "101000111101101"