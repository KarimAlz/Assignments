# n = int(input())
# m = list(map(int,input().split()))

# k = [e for e in set(m) if m.count(e) % 2 != 0]
# print(len(k))
n = int(input())
m = list(map(int, input().split()))

element_counts = {}
for element in m:
    element_counts[element] = element_counts.get(element, 0) + 1

k = [element for element, count in element_counts.items() if count % 2 != 0]
print(len(k))
