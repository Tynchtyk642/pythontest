#1
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31, 55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]
print(dict(enumerate(lst, 1)))


#2
import random 

guesses_made = 0
number = random.randint(1, 20)

while guesses_made < 5:
    guess = int(input('Введите число: '))
    guesses_made += 1

    if guess < number:
        print('слишком мало')

    if guess > number:
        print('слишком много')

    if guess == number:
        break

if guess == number:
    print("Класс! Вы угадали")

else:
    print("Все, вы не выиграли. Игра завершилась")


#3
some_string = "luxurious"

print(some_string[3:6])


#4
a = "get"
b = "put"
c = a[0] + b[0] + a[1] + b[1] + a[2] + b[2]
print(c)