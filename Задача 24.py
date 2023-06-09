#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
#Она растёт на круглой грядке, причём кусты высажены только по окружности.
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
#Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
#Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

N = int(input("Введите количество кустов черники: "))
berry_amounts = []
for i in range(N):
    a = int(input(f'Введите количество ягод на {i+1} кусте: '))
    berry_amounts.append(a)
max_berries = 0
for i in range(N):
    total_berries = berry_amounts[i] + berry_amounts[(i - 1 + N) % N] + berry_amounts[(i + 1) % N]
    if total_berries > max_berries:
        max_berries = total_berries
print("Максимальное число ягод:", max_berries)