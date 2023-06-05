n = int(input("Введите кол-во кустов: "))
na = list()
total = 0

for i in range(n): 
    num = int(input('Введите число ягод на ' + str(i+1) + '-м кусту: ')) 
    na.append(num)
na = na + na[:2] #добавил начало массива в конец
for j in range (2, len(na)):
    total = max(total, na[j] + na[j-1] + na[j-2])

print(total)