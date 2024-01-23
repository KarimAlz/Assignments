import math
n = float(input()) # Tamdan sonra kəsr hissənin görünməsi üçün (sətir 17 də ilk 9 kəsr rəqəmini print eləmək üçün format eləmək lazımdı)

def problem(x):
    return x ** 2 + math.sqrt(x)

def binary_search(n):
    low, high = 1, 10 ** 10
    while low < high:
        mid = (low + high) / 2 # bu məsələdə dəqiq qiymət istədiyi üçün qalıqsız bölmə yox, normal bölmədən istifadə olunur
        if problem(mid) * (10 ** 6) < n * (10 ** 6):
            low = mid + 1
        else:
            high = mid
    return low

print(format(binary_search(n), '.9f'))