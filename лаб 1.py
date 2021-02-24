import random
import time

#Быстрая Сортировка
#ВЫбираем произвольный злемент массива q, делим массив на части, 
#в левой то что меньше выбранного элемента q, в центре, то что равно q, правая часть то, что больше q
# левую и правую часть сортируем по отдельности
def quicksort(mass):
    # Возвращаем значение злемента если длина чати равна 1
   if len(mass) <= 1:
       return mass
   else:
       #выбираем произвольный злемент массива
       q = random.choice(mass)
       # левая,центральная и правая часть
       left_mass = []
       center_mass = []
       right_mass = []
       #распихиваем по частям все злементы массива
       for n in mass:
           if n < q:
               left_mass.append(n)
           elif n > q:
               right_mass.append(n)
           else:
               center_mass.append(n)
        #возращаем Отсортированный массив, заметим что левая и правая часть сотрируются!
       return quicksort(left_mass) + center_mass + quicksort(right_mass)
       
#Сортировка вставкой
def insertionsort(mass):
    #Новый массив
    new_mass = []
    #Проходимся по каждому  замету массива и вставляем его в нужную позицию в новом массиве
    for i in range(len(mass)):
        # print(new_mass)
        
        
        flag = True
        #Ищем куда вставить элемент
        for j in range(len(new_mass)):
            if(new_mass[j] > mass[i]):
                new_mass =  new_mass[:j] + [mass[i]] + new_mass[j:]
                flag = False
                break
        # Данный if сработает если вставить элемент нужно в конец
        if(flag):
            new_mass.append(mass[i])
            
    return new_mass

# print("Введите размер массива")
# n = int(input())


n = 10000
print("Размер массива = " + str(n))

mass = []
for i in range(n):
    mass.append(random.randrange(-n,n))

mass_sort = sorted(mass)    
mass_reverse_sort = sorted(mass, reverse=True)


# print("Наш массив")
# print(mass)
# print("Отсортированный вариант")
# print(mass_sort)
# print("Обратная отсортированный вариант")
# print(mass_reverse_sort)



print("______________________")

print("Сортировка произвольно-заполненного массива")

t1 = time.time()
insertionsort(mass)
t2 = time.time()

print("Сортировка вставкой выполнена за " + str(t2-t1) + " сек")

t1 = time.time()
quicksort(mass)
t2 = time.time()

print("Быстрая сортировка выполнена за " + str(t2-t1) + " сек")

t1 = time.time()
sorted(mass) 
t2 = time.time()

print("Стандартная сортировка выполнена за " + str(t2-t1) + " сек")

print("______________________")

print("Сортировка отсортированного массива")

t1 = time.time()
insertionsort(mass_sort)
t2 = time.time()

print("Сортировка вставкой выполнена за " + str(t2-t1) + " сек")

t1 = time.time()
quicksort(mass_sort)
t2 = time.time()

print("Быстрая сортировка выполнена за " + str(t2-t1) + " сек")

t1 = time.time()
sorted(mass_sort) 
t2 = time.time()

print("Стандартная сортировка выполнена за " + str(t2-t1) + " сек")


print("______________________")

print("Сортировка обратно-отсортированного массива")

t1 = time.time()
insertionsort(mass_reverse_sort)
t2 = time.time()

print("Сортировка вставкой выполнена за " + str(t2-t1) + " сек")

t1 = time.time()
quicksort(mass_reverse_sort)
t2 = time.time()

print("Быстрая сортировка выполнена за " + str(t2-t1) + " сек")

t1 = time.time()
sorted(mass_reverse_sort) 
t2 = time.time()

print("Стандартная сортировка выполнена за " + str(t2-t1) + " сек")

# print(quicksort(mass))

# print(insertionsort(mass))








