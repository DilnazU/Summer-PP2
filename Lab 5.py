import re

# 1. Matches a string that has an 'a' followed by zero or more 'b's
def ab(text):
    pattern = r'ab*'
    return bool(re.fullmatch(pattern, text))

# 2. Matches a string that has an 'a' followed by two to three 'b's
def a23b(text):
    pattern = r'ab{2,3}'
    return bool(re.fullmatch(pattern, text))

# 3. Find sequences of lowercase letters joined with a underscore
def az_(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)

# 4. Find the sequences of one upper case letter followed by lower case letters
def Aa(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)

# 5. Matches a string that has an 'a' followed by anything, ending in 'b'
def a__b(text):
    pattern = r'a.*b$'
    return bool(re.fullmatch(pattern, text))

# 6. Replace all occurrences of space, comma, or dot with a colon
def colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)

# 7. Convert snake case string to camel case string
def snake_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# 8. Split a string at uppercase letters
def split(text):
    return re.findall('[A-Z][^A-Z]*', text)

# 9. Insert spaces between words starting with capital letters
def insert(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

# 10. Convert a given camel case string to snake case
def camel_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()