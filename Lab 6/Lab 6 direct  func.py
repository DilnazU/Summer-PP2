import os  
import string 
import shutil

#Write a Python program to list only directories, files and all directories, files in a specified path.
x = input("Введите путь: ")  
print("директории:")
print([d for d in os.listdir(x) if os.path.isdir(os.path.join(x, d))])
print("файлы:")
print([f for f in os.listdir(x) if os.path.isfile(os.path.join(x, f))])
print("объекты:")
print(os.listdir(x))

#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
x = input("Введите путь: ")  

print("Существует ли путь:", os.path.exists(x))       
print("Доступен к чтению:", os.access(x, os.R_OK))  
print("Доступен для записи:", os.access(x, os.W_OK))  
print("Доступен для выполнения:", os.access(x, os.X_OK))

#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path

x = input("Введите путь: ")  
if os.path.exists(x):  
    print("Путь существует") 
    print("Имя файла:", os.path.basename(x))  
    print("Директория:", os.path.dirname(x)) 
else:
    print("Пути нет")  

#Write a Python program to count the number of lines in a text file
x= input("Введите путь : ")  
try:
    with open(x, 'r', encoding='utf-8') as file:  
        line_count = sum(1 for line in file)  
    print("Кол во строк в файле равно :", line_count)  
except FileNotFoundError: 
    print("Файл не найден")

#Write a Python program to write a list to a file
x = input("Введите путь: ") 
y = input("Введите элементы списка через запятую пожалуйста: ").split(',')  

with open(x, 'w', encoding='utf-8') as f: 
    for item in y: 
        f.write(f"{item.strip()}\n")  

print(f"ВАш список записан в файле: {x}")  

#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt 
for letter in string.ascii_uppercase:  
    with open(f"{letter}.txt", 'w') as f: 
        f.write(f"This is file {letter}.txt\n")  

print ("Файлы начиная с A.txt до Z.txt созданы")  

#Write a Python program to copy the contents of a file to another file

x = input("Введите путь к первому файлу: ") 

y = input("Введите путь к новому файлу: ")  

try:
    shutil.copyfile(x, y) 
    print(f"Содержимое файла скопировано из {x} в {y}")  
except FileNotFoundError: 
    print("Первый файл не найден.")


#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
x = input("Введите путь к файлу который нужно удалить : ")  

if os.path.exists(x):  
    if os.access(x, os.W_OK):  
        os.remove(x)  
        print("Файл удалён")
    else:
        print("Нет прав на удаление файла") 
else:
    print("Файл не существует")  
