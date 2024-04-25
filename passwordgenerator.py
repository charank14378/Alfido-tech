import random
lower='abcdefghijklmnopqrstuvwxyz'
upper=lower.upper()
symbols='!@#$%^&*()_=+-[]}{;:/?><.,'
num='1234567890'
all=lower+upper+symbols+num
length=5
password='cherry'
for i in range(length):
    password=''.join([password,random.choice(all)])
print("Random generated password is",password)
