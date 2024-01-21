# m = 4
# n = 5
# p = [
#     2, 3, 5, 7, 9,   # M x N ölçüsündə cədvəl verilir ("Hardcode" üsulu)
#     3, 6, 9, 11, 13,
#     1, 3, 7, 9, 10,
#     3, 3, 4, 8, 9,
# ]
count = 0
number = []
p = [int(num) for num in input().split()]  # Cədvəl daxil olur (İstənilən cədvəl) (Ayrı-ayrı)
# p = [int(num) for num in str(input())]   # (Bitişik)
m = int(input()) # Sətirlərin sayı
n = int(input()) # Sətrdə ədədlərin sayı

for i in range(int(len(p) / m)):
	count = 0
	for j in range(1, m):
		for k in range(n):
			if int(p[i]) == int(p[k + n * j]):
				count += 1
			if count == m - 1:
				number.append(p[i])
				break
print(number)