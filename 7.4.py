# 7.4 Форматирование строк
# Задача Мастера кода и Волшебники данных

team1 = '<Мастера кода>'
team2 = '<Волшебники данных>'

team1_num = 5  # количество участников 1 команды
team2_num = 6 # количество участников 2 команды

score_1 = 40 # количество задач, решённых командой 1
score_2 = 42 # количество задач, решённых командой 2

team1_time = 1552.512 # время за которое команда 1 решила задачи
team2_time = 2153.31451   # время за которое команда 2 решила задачи

# Использование %:
print('1 - В команде %s участников %s!' % (team1, team1_num))
print('2 - Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

# Использование format():
print('3 - Команда {} решила задач: {}!'.format(team2, score_2))
print('4 - {} решили задачи за {:.2f} секунды!'.format(team2, team2_time))

# Использование f-строк:
tasks_total = score_1 + score_2  # количество задач
time_avg=(team1_time + team2_time) / tasks_total # среднее время решения задачи

print(f'5 - Команды решили {score_1} и {score_2} задач.')
# if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
if team1_time // (team1_num * score_1) < team2_time // (team2_num * score_2):
    print(f'6 - Результат битвы: победа команды {team1}!')
# elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
elif team1_time // (team1_num * score_1) > team2_time // (team2_num * score_2):
    print(f'7 - Результат битвы: победа команды {team2}!')
else:
    print(f'Ничья')
print(f'8 - Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!')

print(f'\nКаждый из {team1} затратил {team1_time // (team1_num * score_1)} сек. на задачу.')
print(f'Каждый из {team2} затратил {team2_time // (team2_num * score_2)} сек. на задачу.')