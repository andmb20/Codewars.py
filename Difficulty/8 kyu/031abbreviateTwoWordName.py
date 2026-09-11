def abbrev_name(name):
    #return name.split()
    return name.upper().split()[0][0] + '.' + name.upper().split()[1][0]

print(abbrev_name("Sam Harris"))# "S.H"
print(abbrev_name("patrick feenan"))# "P.F"
print(abbrev_name("Evan C"))# "E.C"
print(abbrev_name("P Favuzzi"))# "P.F"
print(abbrev_name("David Mendieta"))# "D.M"