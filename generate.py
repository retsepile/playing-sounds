import random, string

my_letters = []

for y in range(5):
    x = random.choice(string.ascii_uppercase)

    my_letters.append(x)
if x not in my_letters:
    my_letters.append(x)
else:
    y = y-1

print(my_letters)
