n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))
na = list()
ma = list()

for i in range(n): 
    num = int(input('Введите '+ str(i+1) +'-е число для первого множества: ')) 
    na.append(num) 
for i in range(m): 
    num = int(input('Введите '+ str(i+1) +'-е число для второго множества: ')) 
    ma.append(num) 
nwr = set(na) #первое множество без повторений
mwr = set(ma) #второе множество без повторений
f = nwr.intersection(mwr) #пересечение множеств
if f != set():
    print("Все числа, которые встречаются в обоих наборах:", sorted(f))
else:
    print("Нет совпадений между множествами")