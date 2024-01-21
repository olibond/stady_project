import random
def generate_password(lenght, chars):
    password = ''
    for i in range(lenght):
        password += random.choice(chars)
    print(password)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = lowercase_letters.upper()
punctuation = '!#$%&*+-=?@^_'
chars = ''

q1 = int(input('How much password do you need?'))
q2 = int(input('How long passwords?'))
q3 = input('Numbers included? y = yes / n = no').lower()
q4 = input('Upper case included? y = yes / n = no').lower()
q5 = input('Lower case included? y = yes / n = no').lower()
q6 = input('Special signs  included? y = yes / n = no').lower()
q7 = input('Should ambiguous characters be excluded? (il1Lo0O) y = yes / n = no').lower()

if q3 == 'y':
    chars += digits
if q4 == 'y':
    chars += uppercase_letters
if q5 == 'y':
    chars += lowercase_letters
if q6 == 'y':
    chars += punctuation
if q7 == 'y':
    for _ in 'il1Lo0O':
        chars.replace(_, '')

for _ in range(q1):
    generate_password(q2, chars)