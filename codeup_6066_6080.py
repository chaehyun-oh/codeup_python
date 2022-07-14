#codeup_6066

a, b, c = map(int, input().split())

if a % 2 == 0:
    print('even')
else:
    print('odd')
if b % 2 == 0:
    print('even')
else:
    print('odd')
if c % 2 == 0:
    print('even')
else:
    print('odd')

#codeup_6067

a = int(input())

if a < 0 :
    if a % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if a % 2 == 0:
        print('C')
    else:
        print('D')

#codeup_6068

n = int(input())

if n >= 90:
    print('A')
else:
    if n >= 70:
        print('B')
    else:
        if n >= 40:
            print('C')
        else:
            print('D')


#codeup_6069

n = input()

if n == 'A':
    print('best!!!')
else:
    if n == 'B':
        print('good!!')
    else:
        if n == 'C':
            print('run!')
        else:
            if n == 'D':
                print('slowly~')
            else:
                print('what?')

            
#codeup_6070

n = int(input())
if n // 3 == 1:
    print('spring')
else:
    if n // 3 == 2:
        print('summer')
    else:
        if n // 3 == 3:
            print('fall')
        else:
            print('winter')

#codeup_6071

n = 1
while n != 0:
    n = int(input())
    if n != 0:
        print(n)

#codeup_6072

n = int(input())
while n != 0:
    print(n)
    n -= 1

#codeup_6073

n = int(input())
while n > 0:
    n -= 1
    print(n)

#codeup_6074

n = ord(input())
t = ord('a')
while t <= n:
    print(chr(t), end=' ')
    t += 1


#codeup_6075

n = int(input())
for i in range(n+1):
    print(i)

#codeup_6076

n = int(input())
for i in range(n+1):
    print(i)

#codeup_6077

n = int(input())
s = 0
for i in range(n+1):
    if i % 2 == 0:
        s += i
print(s)

#codeup_6078

n = 0
while n != 'q':
    n = input()
    print(n)

#codeup_6079

n = int(input())
s = 0
for i in range(n+1):
    s += i
    if s >= n:
        print(i)
        break

#codeup_6080

n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i,j)

#codeup_6081



#codeup_6082
#codeup_6083
#codeup_6084
#codeup_6085
#codeup_6086
