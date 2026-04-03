#root는 **0.5

def root(a,b,c):
    if -b+(b**2.0-4.0*a*c) < 0:
        return None, None
    else:
        x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
        x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
        return x1,x2
r1,r2 = root(1,2,3) #실수해가 없다
print(r1,r2)

def root0(a,b,c):
        x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
        x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
        return x1,x2
r1,r2 = root(1,2,3) 
print(r1,r2)
if type(r1) == complex:
    print('허수입니다.')

def root1(a,b,c):
    if -b+(b**2.0-4.0*a*c)<0:
        return None, None
    x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    return x1,x2

def root2(a,b,c):
    if -b+(b**2.0-4.0*a*c)<0:
        return None, None
    else:
        x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
        x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
        return x1,x2

#root1과 root2는 차이가 없다.
#함수는 return하면 끝난다. (이미 output을 준거다.)
