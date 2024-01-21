# Ədədin sadə bölənlərinin cəmini hesablayır

def prime_factor_sum(a):
    f = []
    f_sum = 0
    i = 2
    while a > 1:
        if a % i == 0:
            a = a / i        
            f.append(i)
            i = 2
        else:
            i += 1
    for i in range(len(f)):
        f_sum += f[i]
    return f_sum

n = int(input())
print(prime_factor_sum(n))