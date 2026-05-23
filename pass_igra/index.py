import random
from random import randint 

def generate():
 asi = random.randint(0000,9999) # генерируем
 global a
 a = int(f"{asi:04}")
 
 last_num = int(str(a)[-1])  # узнаем последнюю цифру
 
 sum_2last = int(str(a)[-1]) + int(str(a)[-2])# цзнаем сумму последниз двух цифр
 
 count = 0
 for i in str(a):
     if int(i) % 2 == 0:
         count += 1 # узнаем все четные
 
 sum_all=0
 for i in str(a):
  sum_all += int(i) #узнаем сумму всез цифр
 
 uslovii = f"\n\n---- ДАННЫЕ ДЛЯ ВЗЛОМА ----\n> Сумма цифр: {sum_all}\n> Четных цифр: {count}\n> Сумма последних двух цифр: {sum_2last}\n> Последняя цифра: {last_num}\n---------------------------\n0 - exit\n\nФормат числа : 0000"
 
 print(uslovii)
 #print(f"Ответ: {a}"") # выводим число
 
def inpts(): 
 try:
  global inp 
  inp = int(input('>> '))
 except:
  print("invalid parament")
  inpts()
  
  
  
generate()
inpts() 


while (inp != 0):
 if (a == inp):
  print("You win!")
  generate()

 else:
  print("Try again !")
 inpts()