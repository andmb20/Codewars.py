def how_much_i_love_you(nb_petals):
    number = ((nb_petals - 1) % 6) + 1
    match number:
        case 1: number = "I love you"
        case 2: number = "a little"
        case 3: number = "a lot"
        case 4: number = "passionately"
        case 5: number = "madly"
        case 6: number = "not at all"
    return number 

print(how_much_i_love_you(7))# "I love you"
print(how_much_i_love_you(3))# "a lot"
print(how_much_i_love_you(6))# "not at all"