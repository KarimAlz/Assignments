j = [h for h in input().split()]
a, b, n = int(j[0]), int(j[1]), int(j[2])
# Bunu bir sətrdə vermək üçün:
# a, b, n = map(int, input().split())

def gcd(a, b): # ƏBOB(a, b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b) # ƏKOB(a, b)

def count_divisible_numbers(a, b, mid):
    return mid // a + mid // b - mid // lcm(a, b)
# Bu funksiyada "mid // a" - dan "mid" - ın "a" - ya böldükdən alınan ədədlərin sayı
# "mid // b" - də isə "b" - yə böldükdən alınan ədədlərin sayısıdı
# Onlar toplanır amma "mid // lcm(a, b)" çıxılır ki, həm "a" - ya, həm də "b" - yə bölmədən alınan ədədləri təkrar saymasın
# Yəni məsələn: a = 2  b = 5 olarsa 10 həm "a" - ya, həm də "b" - yə bölünür, onun 2 dəfə sayılmasının qarşısını almaq üçün "mid // ƏKOB(a, b)" çıxılır (bu kodu ChatGPT - dan götürdüm)

def find_nth_divisible_number(a, b, n):
    low, high = 1, 10 ** 9 # Şərtdə verilir ki maksimum qiymət 10^9 ola bilər və müsbət ədəddir
    
    while low < high: # Binary search alqoritmi
        mid = (low + high) // 2
        if count_divisible_numbers(a, b, mid) < n: # count_divisible_numbers(a, b, mid) indiki orta ədədin a, b -  yə bölünmədən alınan ədədlərin sayını verilən n - ə müqayisə edir
            low = mid
        else:
            high = mid
    
    return low

print(find_nth_divisible_number(a, b, n))

# i = 0 (adi alqoritm (məncə daha sadə və qısadı amma dövrlərə görə zaman xətası verir))
# m = 1
# k = 0
# while i != n:
#     if m % a == 0 or m % b == 0:
#         i += 1
#         k = m
#         m += 1
#     elif m % a != 0 or m % b != 0:
#         m += 1

# print(k)