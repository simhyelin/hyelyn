score = [87, 84, 95, 67, 88, 94, 63]
print(score)
print(type(score))

score = [87, 84, 95, 67, 88, 94, 63]
for i in score:
    print(i)

score = [87, 84, 95, 67, 88, 94, 63]
names = ["영호", "순자", "영식", "순희"]
for i in names:
    print(i)
#여기서 i는 숫자가 아닌 문자열이다.

score = [87, 84, 95, 67, 88, 94, 63]
names = ["영호", "순자", "영식", "순희", score]
for i in names:
    print(i)

score = [87, 84, 95, 67, 88, 94, 63]
names = ["영호", "순자", "영식", "순희", score]
addessbook = [["영호", 25, "010-3825-0000"],["철수", 30, "010-3325-0001"]]
for i in addessbook:
    print(i)

ri = list(range(5))
print(ri)

myString = "apple"
for ch in myString:
    print(ch)
#for 뒤에 range,list,문자열을 넣을 수 있다.

myString = "apple"
for ch in myString:
    print(ch)
listString = list(myString)
print(listString)
#글자 하나하나가 list변수가 되었다.

n_list = [10, 20, 30, 40]
n_list.append(50)
print(n_list)

n_list = [11, 22, 33, 44, 55, 66]
print(n_list)
n_list.remove(44)
print(n_list)
#print는 output이 없는 함수이다.
#remove는 output이 없다.
#pop은 output이 있다.

n_list = [11, 22, 33, 44, 55, 66]
a = n_list.pop()
print(a)
print(n_list)

n_list = [11, 22, 33, 44, 55, 66]
a = n_list.pop()
a = n_list.pop()
print(a)
print(n_list)

a_list = [10, 20, 30, 40]
print(10 in a_list)
print(10 not in a_list)

list1 = [20, 10, 40, 50, 30]
print(min(list1))
print(list1.sort())
list1.sort(reverse = True)
print(list1)

list1 = [20, 10, 40, 50, 30]
list2 = sorted(list1)
print(list1)
print(list2)
#list2는 정리되어서 나온다.

list1 = [1, 2, 3, 4]
list2 = [2, 3, 3, 4]
print(list1 < list2)
#앞의 숫자부터 비교한다.

