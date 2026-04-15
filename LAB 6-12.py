def tuple_sum(tup):
    if isinstance(tup, int):
        return tup
    else:
        accum = 0
        for element in tup:
            accum += tuple_sum(element)
    return accum
def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res | {(i,j)}
    return res
def exp(input_set, exponent):
    res = input_set
    for _ in range(exponent-1):
        res = product_set(res, input_set)
    return res

tuple = {1, 2, 3, 4, 5, 6}
tuple_3times = exp(tuple, 3)
print("주사위를 세 번 던져 발생할 수 있는 사건은", len(tuple_3times), "가지 경우가 존재합니다.")

count_10_over = 0
for case in tuple_3times:
    if tuple_sum(case) >= 10:
        count_10_over += 1
print("주사위를 세 번 던져 나온 눈의 합이 10 이상인 경우는", count_10_over, "가지입니다.")

total_tuple = len(tuple_3times)
def prob_over(x):
    count = 0
    for case in tuple_3times:
        if tuple_sum(case) >= x:
            count += 1
    return (count/total_tuple) * 100
for x in range(3, 19):
    probability = prob_over(x)
    print(f"눈의 합으로 {x:2d} 이상을 얻을 확률 {probability:6.2f}%")
