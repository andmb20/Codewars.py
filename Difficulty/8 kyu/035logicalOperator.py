def xor(a,b):
    if  a == True and b == True:
        return False 
    elif a == True or b == True:
        return True
    else:
        return False

print(xor(False, False))# False, "False xor False == False"
print(xor(True, False))# True, "True xor False == True"
print(xor(False, True))# True, "False xor True == True"
print(xor(True, True))# False, "True xor True == False"