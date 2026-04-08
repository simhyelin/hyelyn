person = {'이름' : '홍길동', '나이' : 26, '몸무게' : 82}
print(person['이름'])
print(person['나이'])
print(person['몸무게'])
#딕셔너리추가하는법
person['국적'] = '대한민국'
print(person)
print(person.keys())
print(person.values())
for key in person:  #person이라는딕셔너리변수에서key를받아온다.
    print('{} : {}'.format(key,person[key]))  #'{} : {}'는 위치를 고정해주는 역할을 한다.

students = { 2019001:'이순신', 2019002:'김유신', 2019003:'강감찬'}
print(students[2019001])
print(students[2019002])
print(students[2019003])
