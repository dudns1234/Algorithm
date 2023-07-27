li = []
li2 = []

# for i in range(200,210):
#     li.append(str(i))
#     print(type(i))


# for j in li:
#     if j[0] % 2 == 0 :
#         li2.append(str(i))
#     elif j[1] % 2 == 0 :
#         li2.append(str(i))
#     elif j[2] % 2 == 0 :
#         li2.append(str(i))

# print(',',join(li2))


for i in range(100,301):
    if int(str(i)[0]) % 2 == 0 and int(str(i)[1]) % 2 == 0 and int(str(i)[2]) % 2 == 0:
        li2.append(str(i))

print(','.join(li2))

    