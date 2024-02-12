n, k = map(int, input().split())
l = [eded for eded in map(int, input().split())]
b = 0

for i in range(n):
    j = 0
    while j < n and max(l[j:j + i + 1:]) - min(l[j:j + i + 1]) <= k :
        print(l[j:j + i + 1:])
        j += 1
        b += 1
    print('keks', l[j:j + i:])
    print('done')

print(b)

# while i <= n:
#     j = 0
#     c_max = max(l[j:j + i:])
#     c_min = min(l[j:j + i:])
#     print(l[j:j + i:])
#     while c_max - c_min <= k:
#         b += 1
#         j += 1
#         c_max = max(l[j:j + i:])
#         c_min = min(l[j:j + i:])
#     i += 1
#     print('done')