src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [i for i in src if src.count(i) == 1]  так делать нельзя - дорого)

set_1 = set()
set_2 = set()
for i in src:
    if i in set_1:
        if i in set_2:
            set_2.discard(i)
    else:
        set_1.add(i)
        set_2.add(i)
result = [el for el in src if el in set_2]
print(result)
