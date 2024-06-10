import random 

def generate_random_numbers(min_range: int, max_range: int) -> list:
    """
    Генерация списка из 3 случайных чисел в пределах указанного диапазона.

    Args:
        min_range (int): Минимальное значение в диапазоне.
        max_range (int): Максимальное значение в диапазоне.

    Returns:
        list: Список из 3 случайных чисел в пределах указанного диапазона.
    """
    return random.sample(range(min_range, max_range + 1), 3)


def comparing_numbers(secret_numbers: set, guessed_numbers: set) -> int:
    """
    Сравнение набора секретных чисел с набором угаданных чисел и
    возращает количество правильных чисел.

    Args:
        secret_numbers (set): Набор секретных чисел.
        guessed_numbers (set): Набор угаданных чисел.

    Returns:
        int: Количество правильных чисел.
    """
    return len(secret_numbers.intersection(guessed_numbers))


def play_game():
    """
    Запускает игру на угадывание чисел.
    """
    min_range = 5
    max_range = 30

    while True:
        user_input = input(f'Введите диапазон чисел (минимум {min_range}, максимум {max_range}): ')
        if user_input == 'exit':
            print('Выход из игры.')
            return
        try:
            min_input_numbers, max_input_numbers = map(int, user_input.split())
            if min_input_numbers < min_range or max_input_numbers > max_range \
                or min_input_numbers >= max_input_numbers:
                print('Некоректный диапазон чисел! Попробуйте снова.')
            else:
                break
        except ValueError:
            print('Некоректный диапазон чисел! Попробуйте снова.')

    secret_numbers = set(generate_random_numbers(min_input_numbers, max_input_numbers))

    while True:
        user_input = input('Пожалуйста введите три числа через пробел или "exit" для выхода из игры: ')
        if user_input == 'exit':
            print('Выход из игры.')
            return
        try:
            guessed_numbers = set(map(int, user_input.split()))
            if len(guessed_numbers) != 3:
                print('Вы ввели не три числа! Попробуйте снова.')
                continue
            if any(numbers < min_input_numbers or numbers > max_input_numbers \
                for numbers in guessed_numbers):
                print(f'Введите числа из диапазона  {min_input_numbers}-{max_input_numbers}: ')
                continue

            correct_count = comparing_numbers(secret_numbers, guessed_numbers)
            print(f'Вы угадали {correct_count} чисел.')

            if correct_count == 3:
                print('You Win!')
                return
            else:
                print('Try again!')
        except ValueError:
            print('Некоректный ввод! Попробуйте снова.')


play_game()
