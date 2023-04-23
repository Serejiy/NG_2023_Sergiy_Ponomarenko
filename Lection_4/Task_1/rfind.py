import argparse
import os

def find_files(folder, file_name):
    """
    Функция для поиска файлов с указанным именем в указанной папке
    и ее подпапках. Возвращает список найденных файлов.
    """
    found_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file_name in file:
                found_files.append(os.path.join(root, file))
    return found_files

# Создание объекта парсера для аргументов командной строки
parser = argparse.ArgumentParser(description='Поиск файлов в папке')
parser.add_argument('--folder', type=str, help='Путь к папке, в которой нужно искать файлы')
parser.add_argument('--file', type=str, help='Имя файла для поиска')

# Парсинг аргументов командной строки
args = parser.parse_args()

# Вызов функции для поиска файлов и вывод результатов
if args.folder and args.file:
    files = find_files(args.folder, args.file)
    if files:
        print(f'Найдено {len(files)} файлов:')
        for file in files:
            print(file)
    else:
        print(f'Файлы с именем "{args.file}" не найдены в папке "{args.folder}".')
else:
    print('Укажите путь к папке и имя файла для поиска.')
