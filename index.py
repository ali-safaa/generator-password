from random import choice
def genPass(data):
    gen = ""
    password = "123456789abcdefg%$&@!"
    for i in range(data):
        gen += choice(password)
    return gen
print(genPass(8))