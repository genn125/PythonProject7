# 7.5 "Файлы в операционной системе"
# Освоить работу с файловой системой в Python, используя модуль os.

from os import walk
from os.path import join, getmtime, getsize, dirname
from time import strftime, localtime


directory = 'D:\\1'

for root, dirs, files in walk(directory): # os.walk более полная информации о структуре директорий и вложенности
    for file in files:
        filepath = join(root, file)  # Путь - объединяет и учитывает разделители путей для разных операционных систем
        filetime = getmtime(filepath)   # Время в виде числа с плавающей точкой, представляющего секунды
                                        # с начала эпохи (обычно это 01.01.1970 г.)
        formatted_time = strftime("%d.%m.%Y %H:%M", localtime(filetime))  # Возвращает удобочитаемую дату от начала
        file_size = getsize(filepath)   # Размер файла по пути
        parent_dir = dirname(filepath)  # Путь к директории, а не к файлу

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')





