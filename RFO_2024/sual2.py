m = [k for k in str(input())]
n = len(m)
k = 0

for i in range(n):
    for j in range(i + 1, n):
        if i + j > n:
            break
        if m[i] != m[j]:
            k += 1
            print(m[i] + m[j])
            break
        else:
            pass

print(k)