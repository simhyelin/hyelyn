for i in range(2, 10):
    for j in range(1, 10):
        print('{}*{} = {:2d}'.format(i, j, i*j), end = ' ')
    print() #빈칸 안에 아무것도 안 쓰면 줄바꿈이다.

for i in range(2, 10):
    for j in range(1, 10):
        print('{}*{} = {:2d}'.format(i, j, i*j), end = ' ')
        print()

n = 7
for i in range(n):
    st = ''
    for j in range(i):
        st = st + ' '
    print(st + '#')

n = 7
for i in range(n):
    print(' '* i + '#')
