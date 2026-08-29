import time
import os
import random
from playsound3 import playsound
import webbrowser

print("Добро пожаловать в систему управления б.я.к\n")

def get_pass():
    global passw
    passw = (__import__('pathlib').Path(__file__).parent / 'pass.txt').read_text(encoding='utf-8')




def show():
    for i in range(8): 
        os.system('cls' if os.name == 'nt' else 'clear')
        a = random.randint(0,180) #угол наклога 
        b = random.randint(-29,100) # температура в градусах
        c = random.randint(10,100) # зашруженность процессора
        print(f"Параметр | Значение\n{'-'* 27}\nУгол наклона | {a}°\nТемпература | {b}°C\nЗагруженность CPU | {c}%")
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()

def gen():
    print("Изменение пароля\nВведите старый, exit для выхода")
    while True:
        old_pass = input(">>")
        get_pass()
        global passw
        if old_pass == passw:
            print("Введите новый пароль")
            (__import__('pathlib').Path(__file__).parent / 'pass.txt').write_text(input('>>'), encoding='utf-8')
            get_pass()
            print("Ваш пароль изменен")
            menu()
            break
        elif old_pass == "exit":
            menu()
            break
        else:
            print("Пароль не верный!")

def activate():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Активация ядерки!!!\nexit для выхода")
    print("Введите пароль")
    while True:
        bpass = input(">>")
        get_pass()
        global passw
        if bpass == passw:
            yorn = input("Вы точно уверены(Y/N): ")
            if yorn =="Y":
                print("Введите координаты")
                coord = input(">>")

                print("Запуск")

                print("1. Финальная проверка систем...")
                time.sleep(0.5)

                print("2. Продувка двигателей...")
                time.sleep(0.5)

                print("3. Дренаж и наддув баков...")
                time.sleep(0.5)

                print("4. Зажигание!")
                time.sleep(0.5)

                print("5. Выход двигателей на максимальную тягу...")
                time.sleep(0.5)

                print("6. КОНТАКТ ПОДЪЁМА! Есть отрыв!")
                time.sleep(1)

                print("7. Выполнение маневра тангажа...")
                time.sleep(2)

                print("8. Прохождение зоны максимального аэродинамического напора (Max-Q)...")
                time.sleep(1)

                print("9. Отсечка двигателей первой ступени...")
                time.sleep(0.5)

                print("10. Разделение ступеней и запуск второй ступени!")

                keys = random.randint(0,2)
                if  keys==2:
                    playsound("sound.mp3", block=False)
                    time.sleep(3)
                    # Звук играет ровно 3 секунды
                    webbrowser.open("https://99px.ru/sstorage/86/2016/12/image_860712162335355416243.gif")
                    time.sleep(10) 
                    break
                else:
                    print('Вы не успели повернуть ключ :(')
                    break
                


            else:
                menu()
                break
        elif bpass == "exit":  # Исправлено: старая переменная old_pass заменена на bpass
            menu()
            break
        else:
            print("Пароль не верный!") 

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Добро пожаловать в меню!\ne - для выхода")
    print("Доступнык команды: \ndata - Данные \ngen_pass - сменить пароь\nactivate- Активация ядерки")
    while True:
        a = input(">>").strip().lower()
        if a=="data":
            show()
            break
        elif a=="e":
            break
        elif a =="gen_pass":
            gen()
            break
        elif a == "activate":
            activate()
            break
        else:
            print("Ошибка!! Не правильный ввод")

def show_loading(seconds=5):
    for i in range(int(seconds / 0.3)):
        print(f"\rЗагрузка системы{'.' * (i % 4):<3}", end="", flush=True)
        time.sleep(0.3)
    print("\rЗагрузка завершена! ")

show_loading(5)
menu()
