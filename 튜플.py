#튜플변수는 list변수와 달리 한 번 만들면 변경할 수 없다.
def plusminus(a1, a2):
    return a1+a2, a1-a2
output = plusminus(10,2) #함수에서 나오는 output은 함부로 변경이 안 된다
print(type(output))

def plusminus(a1, a2):
    return a1+a2, a1-a2
output = plusminus(10,2)
output_list = list(output) #list로 바꾸는 방법
print(type(output_list))

def plusminus(a1, a2):
    return a1+a2, a1-a2
m1,m2 = plusminus(10,2) #정수로 받아들이고 있다.
