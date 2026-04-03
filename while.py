i = 0
while i<5 :
    print('Welcome to everyone!!')
    i += 1 #앞에 무조건 띄어줘야한다.

n = 5
for i in range(n):
    print("Welcome to everyone!!")

isum = 0
n_list = [0, 2, 5, 10]
for i in n_list:
    isum += i
print(isum)

n_list = [0, 2, 5, 10]
isum = 0
i = 0
while i<4:
    isum += n_list[i]
    i += 1
print(isum)
#이 코드는 list의 갯수를 알아야 한다는 문제점이 있다.
#for에서 while로 바꿀 수 있어야한다!

n_list = [0, 2, 5, 10]
isum = 0
i = 0
while i<len(n_list):
    isum += n_list[i]
    i += 1
print(isum)
#len을 이용해 list의 크기를 지정해준다.

