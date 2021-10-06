"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def binary_search(number: int = 1) -> int:
    """Ищем число половинным делением диапазона чисел. 
    Середину диапазона сравниваем с загаданным числом.
    Если не угадали, сдвигаем границу диапазона и снова делим пополам и т.д."""
    count = 1
    left_border = 1  # левая граница диапазона
    right_border = 100  # правая граница диапазона
    predict_number = (right_border + left_border) // 2  # берем середину диапазона
    while number != predict_number:
        count += 1
        if number > predict_number:
            left_border = predict_number + 1  # сдвигаем левую границу
        elif number < predict_number:
            right_border = predict_number - 1  # сдвигаем правую границу
        predict_number = (right_border + left_border) // 2
    return count

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    #score_game(random_predict)
    score_game(binary_search)
