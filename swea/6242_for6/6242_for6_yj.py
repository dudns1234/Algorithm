blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

a_blood = []
b_blood = []
o_blood = []
ab_blood = []

for i in blood:
    if i == "A":
        a_blood.append(i)
    elif i == "O":
        o_blood.append(i)
    elif i == "B":
        b_blood.append(i)
    else:
        ab_blood.append(i)

dict = {
    "A": len(a_blood),
    "B": len(b_blood),
    "O": len(o_blood),
    "AB": len(ab_blood)
}

print(dict)