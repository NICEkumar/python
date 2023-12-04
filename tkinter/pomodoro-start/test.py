import random

newPassword = ''
text = '1234567890qwertyuiopasdfghjklzxcvbnm-_/:!@#$%^&*~<>?'
for i in range(15):
    pos = random.randint(0, len(text)-1)
    newPassword += text[pos]

print(newPassword)