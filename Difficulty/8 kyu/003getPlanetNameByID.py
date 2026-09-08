def get_planet_name(id):
    name = id
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name

print(get_planet_name(2)) # 'Venus'
print(get_planet_name(5)) # 'Jupiter'
print(get_planet_name(3)) # 'Earth'
print(get_planet_name(4)) # 'Mars'
print(get_planet_name(8)) # 'Neptune'
print(get_planet_name(1)) # 'Mercury'