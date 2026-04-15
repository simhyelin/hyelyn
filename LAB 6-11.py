def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i, j)}
    return res
A = {1, 2}
B = {'A', 'B', 'C'}
AxB = product_set(A, B)
BxA = product_set(B, A)
AxA = product_set(A, A)
BxB = product_set(B, B)
print('A =', A)
print('B =', B)
print('AxB =', AxB)
print('BxA =', BxA)
print('AxA =', AxA)
print('BxB =', BxB)
