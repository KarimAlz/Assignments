#Verilmiş N natural ədədi üçün 1-dən böyük olmayan bütün sadə, ixtisar olunmayan kəsrlər ardıcıllığını artan sıra ilə düzən proqram yazın.

def sort(a, b): # Artan sıra ilə düzmək funksiyası
    for i in range(len(a) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                b[j], b[j + 1] = b[j + 1], b[j]
                swapped = True
        if not swapped:
            break


def GCD(a, b): # ƏBOB(a, b)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a != 0:
        c = a
    elif b != 0:
        c = b
    return c


n = int(input())
m = []
l = []

for i in range(n, 0, -1):  # Kəsrin ixtisar olub-olmadığını yoxlayan dövr
    for j in range(1, n):
        if GCD(j, i) == 1 and j / i <= 1:
            m.append(str(str(j) + ' / ' + str(i)))
            l.append(j / i)

sort(l, m)
print(m)