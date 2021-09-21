import string
import random

total = string.ascii_letters + string.digits + string.punctuation +string.hexdigits + string.ascii_uppercase

lenth = 16

password ="".join(random.sample(total, lenth))

print(total)

print(password)
