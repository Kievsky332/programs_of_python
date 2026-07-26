
# Стандартные данные
hour = 0


# Запрашиваем данные

hours = int(input("Введите количество часов: "))
minutes = int(input("Введите количество минут: "))


print("+ сколько часов и минут вы хотите добавить?")

hours_add = int(input("Введите количество часов: "))
minutes_add = int(input("Введите количество минут: "))

# Считаем общее количество минут

count_minutes = minutes + minutes_add
while count_minutes>60:
    hour +=1
    count_minutes -=60
count_hour = hours+hours_add+hour

while count_hour>24:
    count_hour -=24
print(f"{hours:02}:{minutes:02}\n+\n{hours_add:02}:{minutes_add:02}\n=\n{count_hour:02}:{count_minutes:02}")
