from random import gauss, randint


def progression():
    s = (5 / 3)  # величина стандартного отклонения для будущей длины прогрессии (минимум 5 чисел)
    length = round(gauss(10, s))  # если рекомендуемое кол-во чисел 10, то близкие к нему значения будут выпадать чаще
    step = randint(2, 12)  # произвольный интервал для шага прогрессии
    num = randint(1, 50)  # произвольное первое число прогрессии
    numbers = []

    while len(numbers) <= length:
        numbers.append(num)
        num += step

    index = randint(0, length - 1)
    hidden_number = numbers[index]
    numbers[index] = ".."
    print("Question: ", end="")
    print(' '.join(str(n) for n in numbers))
    return hidden_number


GAME_DESCRIPTION = 'What number is missing in the progression?'

if __name__ == "__main__":
    progression()

