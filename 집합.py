set1 = {0, 1, 2, 3, 4, 5, 5}
print(set1)

set1 = {0, 5, 2, 2, 4, 1}
print(set1)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Aset.union(Bset)
print(Cset)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Aset | Bset
print(Cset)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Bset.union(Aset)
print(Cset)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Bset | Aset
print(Cset)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Aset & Bset
print(Cset)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Aset.intersection(Bset)
print(Cset)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Bset & Aset
print(Cset)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Bset.intersection(Aset)
print(Cset)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Aset - Bset
print(Cset)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Aset.difference(Bset)
print(Cset)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Bset - Aset
print(Cset)

Aset = {1, 2, 3, 4}
Bset = {2, 4, 6, 7}
Cset = Bset.difference(Aset)
print(Cset)
