def iplus(x1,x2):
    isum = x1 + x2
    return isum
hap = iplus(4,5) #return이 iplus의 각 함수를 isum으로 바꾸어준다.
print(hap)

def iplus(x1,x2):
    isum = x1 + x2
    print(isum) #여기서는 output이 아니다.
    return isum
hap = iplus(4,5) 
print(hap)

def print_star():
    print('************************')
print_star() #input이 없어도 괄호를 열고 닫아야한다.

a = print_star()
print(a) #output이 없다.

