numbers = [2, 5, 3, 1, 8]
#numbers = [i for i in range(1,13)]

# 부분집합을 구하는 배열의 길이
n = len(numbers)

for i in range(1<<n):
    #print(i, bin(i))

    temp = []
    for j in range(n):
        if i & (1<<j):
            temp.append(numbers[j])

    # print(temp)