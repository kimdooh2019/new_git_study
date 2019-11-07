from random import randint


answer = randint(1, 100+1)
print(answer)
guess = int(input('guess the number :'))

print(guess, type(guess))
# static value is left 
# for remark

for i in range(1, 3+1):

  if guess == answer:
      print('good job')
  else:
      print('nobe')
