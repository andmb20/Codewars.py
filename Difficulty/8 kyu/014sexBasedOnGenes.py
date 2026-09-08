def chromosome_check(chromosome):
    return 'Congratulations! You\'re going to have a son.' if chromosome == 'XY' else 'Congratulations! You\'re going to have a daughter.'

print(chromosome_check('XY'))# 'Congratulations! You\'re going to have a son.'
print(chromosome_check('XX'))# 'Congratulations! You\'re going to have a daughter.'