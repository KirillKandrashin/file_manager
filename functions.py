import os
import shutil


def create_file(p, n, text=None):
    with open(p + n, 'w', encoding='utf-8') as f:
        if text:
            f.write(text+' ')


def create_folder(p, n):
    try:
        os.mkdir(p + n)
    except FileExistsError:
        print('Такая папка уже существует')


def get_list(p, folders_only=False):
    result = os.listdir(p)
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete(p):
    if os.path.isdir(p):
        os.rmdir(p)
    else:
        os.remove(p)


def copy(p, new_p):
    if os.path.isdir(p):
        try:
            shutil.copytree(p, new_p)
        except FileExistsError:
            print('Такая папка уже существует')
    else:
        shutil.copy(p, new_p)


def rename(path, n, new_n):
    os.rename(path + n, path + new_n)


def reading(p):
    f = open(p, 'r')
    reads = f.read()
    f.close()
    print(reads)


def move(p, new_p):
    if os.path.isdir(p):
        try:
            shutil.move(p, new_p)
            delete(p)
        except FileExistsError:
            print('Такая папка там уже существует')
    else:
        shutil.move(p, new_p)
        delete(p)


def writting(p, n, text):
    with open(p + n, 'a', encoding='utf-8') as f:
        if text:
            f.write(text+' ')
