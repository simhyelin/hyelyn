s = 0
for i in range(1,101):
    s = s + i
    print('i = {}, s = {}'.format(i,s))
print('1에서 100까지의 합:', s)

s = 0
for i in range(0,101,2):
    s = s + i
    print('i = {}, s = {}'.format(i,s))
print('1에서 100까지 정수 중에서 짝수의 합:', s)

s = 0
for i in range(1,101,2):
    s = s + i
    print('i = {}, s = {}'.format(i,s))
print('1에서 100까지 정수 중에서 홀수의 합:', s)
