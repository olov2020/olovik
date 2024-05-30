import random
from colorama import init, Fore, Back, Style

# Создаем игровое поле: двумерный список с внешним списком, содержащим n внутренних списков,
# каждый из которых заполнен n пустыми строками
n = 3
playing_field = [[' ' for _ in range(n)] for _ in range(n)]
figures = {
    'X': 'O',
    'O': 'X',
}
error_message = 'Упс... Кажется, ты ввел неверные данные\n'


# Приветственная функция, которая здоровается с пользователем,
# а также реализует функцию "подбрасывания монетки" для определения первенства хода
def welcome():
    global error_message

    print('Привет, дорогой друг!\n'
          'Меня зовут Bot и я хочу сыграть с тобой в крестики нолики)\n'
          'Сейчас я подброшу монетку, которая определит, кто ходит первым. Выбери сторону - орел или решка\n'
          'Для этого введи <орел> или <решка> в консоль')
    # Запрашиваем ввод от пользователя с консоли и преобразуем введенный текст в нижний регистр
    choice_human = input().lower()
    while choice_human != 'орел' and choice_human != 'решка':
        print(f'{error_message}'
              f'Пожалуйста, вводи только <орел> или <решка> (без скобочек, регистр не важен)')
        choice_human = input().lower()

    # Создаем словарь для рандомного выпадения орла/решки
    choices = {
        'орел': 0,
        'решка': 1,
    }
    choice_computer = random.randint(0, 1)

    # Смотрим, совпадает ли наш выбор с рандомайзерным
    move = choices[choice_human] == choice_computer
    if move:
        print('Ты будешь ходить первым')
    else:
        print('Первым хожу я, Bot')

    return move


# Функция прощания с игроком,
# которая также сообщает пользователю о статусе завершения игры: ничье, выигрыше или проигрыше
def bye(state_of_win):
    # проверка на ничью
    if check_draw():
        print('Вау, это была достойная игра...\n'
              'Жду тебя снова!')
        return

    # Проверяем, выиграл ли пользователь и выводим выигрыш, в ином случае выводим проигрыш
    if state_of_win:
        message = 'поздравляю, ты выйграл!'
    else:
        message = 'мне очень жаль, ты проиграл('
    print(f'Спасибо за игру, {message}\n'
          f'До новых встреч!')


# Выбор пользователем фигуры, которой он будет играть
def choice_of_figure():
    global error_message

    print('Настало время выбрать, на какой стороне ты...\n'
          'Если хочешь ставить крестики - введи <1>, если нолики - <0>')

    # Запрашиваем ввод от пользователя и проверяем на вшивость
    choice = input()
    while choice != '1' and choice != '0':
        print(f'{error_message}'
              f'Если хочешь ставить крестики - введи <1>, если нолики - <0> (без скобочек)')
        choice = input()

    message = 'крестиками'
    if not choice:
        message = 'ноликами'
    print(f'Ты ходишь {message}.')

    if choice == '1':
        return 'X'
    return 'O'


# Проверка на выигрыш
def check_win():
    global playing_field, n

    for i in range(n):
        if playing_field[i][0] == playing_field[i][1] == playing_field[i][2] and playing_field[i][0] != ' ':
            return True
        if playing_field[0][i] == playing_field[1][i] == playing_field[2][i] and playing_field[0][i] != ' ':
            return True
    if playing_field[0][0] == playing_field[1][1] == playing_field[2][2] and playing_field[0][0] != ' ':
        return True
    if playing_field[0][2] == playing_field[1][1] == playing_field[2][0] and playing_field[0][2] != ' ':
        return True
    return False


# Проверка на занятость ячейки поля
def check_fill(x, y):
    global playing_field

    if playing_field[x][y] == ' ':
        return False
    # Возвращаем фигуру, которой занята ячейка
    return playing_field[x][y]


# Проверяем на ничью
def check_draw():
    global n

    for i in range(n):
        for j in range(n):
            if not check_fill(i, j):
                return False
    return True


# Проверка того, что пользователь ввел 2 координаты
def check_human_coordinates():
    global error_message

    s = input().split()
    while len(s) != 2 or not s[0].isdigit() or not s[1].isdigit():
        print(f'{error_message}'
              f'Введите 2 координаты через пробел в 1 строку.\n'
              f'Первая координата - номер строки от 1 до 3, вторая координата - номер столбца от 1 до 3')
        s = input().split()

    return [int(s[0]), int(s[1])]


# Проверка, что пользователь ввел валидные координаты,
# также здесь вызывается проверка на 2 координаты (ф-ция выше) и проверка, что ячейка свободна
def check_human_input():
    global error_message, playing_field

    s = check_human_coordinates()
    x, y = s[0], s[1]
    while x not in [1, 2, 3] or y not in [1, 2, 3] or 1 <= x <= 3 and 1 <= y <= 3 and check_fill(x - 1, y - 1):
        if 1 <= x <= 3 and 1 <= y <= 3 and check_fill(x - 1, y - 1):
            print(f'Поле с координатами {x} и {y} занято, введите новые координаты')
        print(f'{error_message}'
              f'Введите 2 координаты через пробел в 1 строку.\n'
              f'Первая координата - номер строки от 1 до 3, вторая координата - номер столбца от 1 до 3')
        s = check_human_coordinates()
        x, y = s[0], s[1]

    return [x - 1, y - 1]


# Реализация логики хода пользователя
def human_move(figure):
    global playing_field

    print('Твой ход - введите координаты клетки, в которую хотите походить.\n'
          'Введите 2 координаты через пробел в 1 строку.\n'
          'Первая координата - номер строки от 1 до 3, вторая координата - номер столбца от 1 до 3')
    coordinates = check_human_input()
    x, y = coordinates[0], coordinates[1]
    playing_field[x][y] = figure
    show(figure)


# Проверка возможности выигрыша следующим ходом пользователя
def check_next_human_move(figure):
    global playing_field, n, figures

    human_figure = figures[figure]

    for i in range(n):
        for j in range(n):
            if playing_field[i][j] == ' ':
                if check_fill(i, (j + 1) % n) == human_figure and check_fill(i, (j + 2) % n) == human_figure:
                    return [i, j]
                if check_fill((i + 1) % n, j) == human_figure and check_fill((i + 2) % n, j) == human_figure:
                    return [i, j]
        if playing_field[i][i] == ' ':
            if check_fill((i + 1) % n, (i + 1) % n) == human_figure and check_fill((i + 2) % n,
                                                                                   (i + 2) % n) == human_figure:
                return [i, i]
            if check_fill((i - 1) % n, (i - 1) % n) == human_figure and check_fill((i - 2) % n,
                                                                                   (i - 2) % n) == human_figure:
                return [i, i]
            if check_fill((i + 1) % n, (i - 1) % n) == human_figure and check_fill((i + 2) % n,
                                                                                   (i - 2) % n) == human_figure:
                return [i, i]
            if check_fill((i - 1) % n, (i + 1) % n) == human_figure and check_fill((i - 2) % n,
                                                                                   (i + 2) % n) == human_figure:
                return [i, i]
        if playing_field[i][n - 1 - i] == ' ':
            if check_fill((i + 1) % n, (n - 1 - i + 1) % n) == human_figure and check_fill((i + 2) % n,
                                                                                           (
                                                                                                   n - 1 - i + 2) % n) == human_figure:
                return [i, n - 1 - i]
            if check_fill((i - 1) % n, (n - 1 - i - 1) % n) == human_figure and check_fill((i - 2) % n,
                                                                                           (
                                                                                                   n - 1 - i - 2) % n) == human_figure:
                return [i, n - 1 - i]
            if check_fill((i + 1) % n, (n - 1 - i - 1) % n) == human_figure and check_fill((i + 2) % n,
                                                                                           (
                                                                                                   n - 1 - i - 2) % n) == human_figure:
                return [i, n - 1 - i]
            if check_fill((i - 1) % n, (n - 1 - i + 1) % n) == human_figure and check_fill((i - 2) % n,
                                                                                           (
                                                                                                   n - 1 - i + 2) % n) == human_figure:
                return [i, n - 1 - i]
    return []


# Реализация логики хода компьютера
def computer_move(figure):
    global playing_field, n

    # Проверка на выигрыш пользователя следующим ходом
    next_move = check_next_human_move(figure)
    if next_move:
        playing_field[next_move[0]][next_move[1]] = figure
        return

    # Массив возможных полей для рандомного хода
    not_fill = []

    for i in range(n):
        for j in range(n):
            if not check_fill(i, j):
                not_fill.append([i, j])

    choice = random.randint(0, len(not_fill) - 1)
    x = not_fill[choice][0]
    y = not_fill[choice][1]
    playing_field[x][y] = figure


# Функция отображения игрового поля с красивым цветным оформлением
def show(figure):
    global playing_field, n

    for _ in range(14):
        print(Fore.YELLOW + f'-', end='')
    print()
    for i in range(n):
        print(Fore.YELLOW + '|', end='')
        for j in range(n):
            color = Fore.GREEN
            if playing_field[i][j] != figure:
                color = Fore.RED
            print(color + f' {playing_field[i][j]} ', end='')
            print(Fore.YELLOW + '|', end='')
        print()

        for _ in range(14):
            print(Fore.YELLOW + f'-', end='')
        print()


# Основная логика программы
def main():
    global figures

    choice_of_move = welcome()  # True if it is humans move

    figure = choice_of_figure()
    computer_figure = figures[figure]

    status_win = False
    # Цикл программы
    while not check_win() and not check_draw():
        if choice_of_move:
            show(figure)
            human_move(figure)
            status_win = True
        else:
            computer_move(computer_figure)
            status_win = False
        choice_of_move += 1
        choice_of_move %= 2

    bye(status_win)
    show(figure)


if __name__ == '__main__':
    main()
