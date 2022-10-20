# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.

number = int(input("Введите число: "))
spisok = list(range(-number, number+1))
print(spisok)
spisok = spisok[2:] + spisok[:2]
print(spisok)