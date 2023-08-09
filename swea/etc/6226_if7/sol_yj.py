li = []

for i in range(201):
    if i % 7 == 0 and i % 5 != 0 :
        li.append(str(i))

print(','.join(li)) # 리스트를 string으로 변환해주는 방법