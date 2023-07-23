n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

list1 = []
list2 = []

print("Введите элементы первого множества:")
for _ in range(n):
    element = int(input())
    list1.append(element)

print("Введите элементы второго множества:")
for _ in range(m):
    element = int(input())
    list2.append(element)

result = sorted(list(set(list1) & set(list2)))

print("Результат:")
for element in result:
    print(element)