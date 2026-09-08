# [:-1]

# Best Approach
# def remove(s):
#     return s[:-1] if s.endswith('!') else s

def remove(s):
    if s == '' or s[-1] != '!':
        return s
    else:
        return s[:-1]

print(remove("Hi!"))# "Hi"
print(remove("Hi!!!"))#"Hi!!"
print(remove("!Hi"))# "!Hi"
print(remove("!Hi!"))# "!Hi"
print(remove("Hi! Hi!"))# "Hi! Hi"
print(remove("Hi"))# "Hi"
print(remove(""))# ""
