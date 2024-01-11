n = str(input())
if int(n) < 100 or int(n) > 999:
    print('False')
else:
    print(n[:0:-1])