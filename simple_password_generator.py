import random
import string

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{}.,-_@#*\\//+ "

#which character should be present in password
upper, lower, numb, symb = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if numb:
    all += digits
if symb:
    all += symbols

length = 10
amount = 20

for x in range(amount):
    password = "".join(random.sample(all, length))

    print(password)

