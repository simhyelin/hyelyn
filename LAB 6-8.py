def square(n1, n2):
    return n1**2, n2**2
x = 10
y = 20
x_sq, y_sq = square(x, y)
print('{} 제곱 = {}, {} 제곱 = {}'.format(x, x_sq, y, y_sq))

t = (10, 20, 30) + (40, 50, 60)
print(t)

print('Hello ' * 3)

print(('Hello ',) * 3)
