#codeup_6040
a, b = map(int, input().split())
print(int(a/b))

#codeup_6041
a, b = map(int, input().split())
print(int(a%b))

#codeup_6042
a = input()
a = float(a)
print(format(a, '.2f'))


#codeup_6043
f1, f2 = map(float, input().split())
print(format(f1/f2, '.3f'))

#codeup_6044
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, '.2f'))

#codeup_6045
a, b, c = map(int, input().split())
total = int(a+b+c)
print(total, format(total/3, '.2f'))

#codeup_6048
a, b = map(int, input().split())
if a < b:
    print('True')
else:
    print('False')

#codeup_6049
a, b = map(int, input().split())
if a == b:
    print('True')
else:
    print('False')

#codeup_6050
a, b = map(int, input().split())
if b >= a:
    print('True')
else:
    print('False')

#codeup_6051
a, b = map(int, input().split())
if a != b:
    print('True')
elif a == b:
    print('False')

#codeup_6052
n = int(input())
print(bool(n))

#codeup_6053
n = bool(int(input()))
print(not n)

#codeup_6054
a, b = map(int, input().split())
if bool(a) and bool(b):
    print('True')
else:
    print('False')

#codeup_6055
a, b = map(int, input().split())
if bool(a) or bool(b):
    print('True')
else:
    print('False')

#codeup_6056
a, b = map(int, input().split())
if bool(a) != bool(b):
    print('True')
else:
    print('False')

#codeup_6057
a, b = map(int, input().split())
if bool(a) == bool(b):
    print('True')
else:
    print('False')

#codeup_6058
a, b = map(int, input().split())
if bool(a) == False and bool(b) == False:
    print('True')
else:
    print('False')

#codeup_6063
a, b = map(int, input().split())
c = a if a >= b else b
print(c)

#codeup_6064
a, b, c = map(int, input().split())
result = (a if a < b else b) if ((a if a < b else b) < c) else c
print(result)

#codeup_6065
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)





