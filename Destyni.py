import random


def destiny_fate(win, loser):
    user_input = input('Should I rest or study:')
    numbers = []  # создать список чисел из 1 to 999
    for i in range(1, 999):
        numbers.append(i)  # генерирует список от 1 до 999

    win1 = random.choice(numbers)
    numbers.remove(win1)
    win2 = random.choice(numbers)
    print(win, loser)
    return win1, win2


# Вызов функции
win1, win2 = destiny_fate("The winning numbers are:", "Your losing number:")
print(win1, win2)