from random import randint


answer = randint(1, 100+1)
print(answer)
guess = int(input('guess the number :'))

print(guess, type(guess))
# static value is left 
if guess == answer:
    print('good job')
else:
    print('nobe')
