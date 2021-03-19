import os
import sys

from functions import create_file, create_folder, get_list, delete, copy, rename, reading, writting

command = sys.argv[1]
if os.name == "nt":
    f = open("path.txt", 'r')
    if "D:/test/" not in f.read():
        print("Вы вышли из рабочей директории и были возвращены!")
        with open("path.txt", "w") as file:
            file.write("D:/test/")
    f.close()
elif os.name == "posix":
    f = open("path.txt", 'r')
    if "~/labs" not in f.read():
        print("Вы вышли из рабочей директории и были возвращены!")
        with open("path.txt", "w") as file:
            file.write("~/labs")
    f.close()

f = open("path.txt", 'r')
path = f.read()
f.close()

if command == 'list':
    try:
        print(path)
        get_list(path)
    except IndexError:
        print('Нет параметра')
elif command == 'go_to':
    try:
        path = path + sys.argv[2] + '/'
        f = open("path.txt", 'w')
        f.close()
        with open("path.txt", "w") as file:
            file.write(path)
    except IndexError:
        print('Нет параметра')
elif command == 'go_back':
    splited_path = path.split("/")
    path = "/".join(splited_path[:-2]) + "/"
    f = open("path.txt", 'w')
    f.close()
    with open("path.txt", "w") as file:
        file.write(path)
elif command == 'create_file':
    try:
        name = sys.argv[2]
        text = sys.argv[3]
    except IndexError:
        print('Нет параметра')
    create_file(path, name, text)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Нет параметра')
    create_folder(path, name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Нет параметра')
    delete(path + name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Необходимо 2 параметра')
    copy(path + name, new_name)
elif command == 'rename':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Необходимо 2 параметра')
    rename(path, name, new_name)
elif command == 'read':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Нет параметра')
    reading(path + name)
elif command == 'move':
    try:
        name = sys.argv[2]
        new_path = sys.argv[3]
    except IndexError:
        print('Необходимо 2 параметра')
    copy(path + name, new_path)
elif command == 'write':
    name = sys.argv[2]
    text = sys.argv[3]
    writting(path, name, text)
else:
    print('Unknown command')
