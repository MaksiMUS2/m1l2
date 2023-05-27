import random

simvol = "(+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890)"

dlina = int(input("Введите длину пароля"))

password = ''

for i in range(dlina):
    password +- random.choice(simvol)

print(password)