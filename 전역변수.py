#지역변수:함수내에서 쓰는 변수
#전역변수:함수밖에서 쓰는 변수, 지역변수에 영향을 주기도 한다.

def print_sum():
    result = a + b
    print('print_sum() 내부 :', a, '과', b, '의  합은', result, '입니다.')
a = 10
b = 20
print_sum()
result = a + b
print('print_sum() 외부 :', a, '과', b, '의 합은', result, '입니다.')
