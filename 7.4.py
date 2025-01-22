# 7.4 Форматирование строк
# Задача Мастера кода и Волшебники данных

team1 = '<Мастера кода>'
team2 = '<Волшебники данных>'

team1_num = 5  # количество участников 1 команды
team2_num = 6 # количество участников 2 команды

score_1 = 40
score_2 = 42

team1_time = 1552.512 # время за которое команда 1 решила задачи
team2_time = 2153.31451   # время за которое команда 2 решила задачи

# Использование %:
print('1 - В команде %s участников %s!' % (team1, team1_num))
print('2 - Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
# Использование format():
print('3 - Команда {} решила задач: {}!'.format(team2, score_2))
print('4 - {} решили задачи за {} c!'.format(team2, team2_time))
# Использование f-строк:
# print(f'5 - Команды решили {score_1} и {score_2} задач')

def challenge_result(tasks_total, time_avg):
    print(f'5 - Команды решили {score_1} и {score_2} задач')
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    # if score_1 > score_2:
        print(f'6 - Результат битвы: победа команды {team1}!')
    else:
        print(f'7 - Результат битвы: победа команды {team2}!')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')

challenge_result(82,45.2)
