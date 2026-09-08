# upper - method is a built-in string function used to convert all lowercase letters in a string to uppercase equivalents.

def sp_eng(sentence): 
    return 'ENGLISH' in sentence.upper()

print(sp_eng("english"))# True
print(sp_eng("egnlish"))# False
print(sp_eng("engliish"))# False
print(sp_eng("1234egn lis;h"))# False
print(sp_eng("1234english ;k"))# True
print(sp_eng("English"))# True
print(sp_eng("eNgliSh"))# True
print(sp_eng("1234#$%%eNglish ;k9"))# True
print(sp_eng("EGNlihs"))# False
print(sp_eng("1234englihs**"))# False