# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй

string1 = input("Введите слово 1: ")
string2 = input("Введите слово 2: ")

for i in range(len(string1)):
    count = 0
    for j in range(len(string2)):
        if string1[i] == string2[j]:
            count += 1
    print(f"{string1[i]} - {count}", end = " , ")