# a = int(input())
# b = int(input())
# if a < b:
#     print(a)
# elif a == b:
#     print("Числа равны")
# else:
#     print(b)

# a = int(input())
# if 1000 <= a <= 9999 or -9999 <= a <= -1000:
#     print('YES')
# else:
#     print('NO')

# a = input()
# if '-' in a:
#     if len(a) == 5:
#         print('YES')
#     else:
#         print('NO')
# else:
#     if len(a) == 4
#         print('YES')
#     else:
#         print('NO')

summa = 0
while True:
    a = input()
    if a == ' ':
        break
    if int(a) % 4 == 0:
        summa += int(a)
print(summa)
