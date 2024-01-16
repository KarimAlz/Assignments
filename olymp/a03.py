# A03. X və Y dəyişənlərinin qiymətlərini elə paylayın ki, X onların böyüyü, Y isə kiçiyi olsun.
n = input()
x, y = n.split()
if int(x) > int(y):
    print(x, y)
else:
    print(y, x)