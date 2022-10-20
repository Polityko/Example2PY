# Задача 1. Напишите программу, которая принимает на вход число N и выдает список 
# факториалов для чисел от 1 до N.

N = int(input("Введите число: "))
result = []
factorial = 1

for i in range(1, N+1):
    factorial *= i
    result.append(factorial)
    
print(result)