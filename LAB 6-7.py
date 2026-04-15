t_person = ('홍길동', 2019001, 179)
print('t_person=', t_person)
t_person_list(1) == 2019003
t_person_list = list(t_person)
t_person_list[1] = 2020003
t_person = tuple(t_person_list)
print(f"학번 변동 후 t_person = {t_person}")
