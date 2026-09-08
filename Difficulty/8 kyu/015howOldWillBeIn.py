def calculate_age(year_of_birth, current_year):
    if current_year < year_of_birth:
        if year_of_birth - current_year == 1:
             return 'You will be born in 1 year.'
        else:
            return 'You will be born in ' + str(year_of_birth - current_year) + ' years.'
    elif current_year > year_of_birth:
        if current_year - year_of_birth == 1:
            return 'You are 1 year old.'
        else:
            return 'You are ' + str(current_year - year_of_birth) + ' years old.'
    else:
        return 'You were born this very year!'

print(calculate_age(2012, 2016))# "You are 4 years old."
print(calculate_age(1989, 2016))# "You are 27 years old."
print(calculate_age(2000, 2090))# "You are 90 years old."
print(calculate_age(2000, 1990))# "You will be born in 10 years."
print(calculate_age(2000, 2000))# "You were born this very year!"
print(calculate_age(900, 2900))# "You are 2000 years old."
print(calculate_age(2010, 1990))# "You will be born in 20 years."
print(calculate_age(2010, 1500))# "You will be born in 510 years."
print(calculate_age(2011, 2012))# "You are 1 year old."
print(calculate_age(2000, 1999))# "You will be born in 1 year."