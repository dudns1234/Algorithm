my_list = [1,6,3,9,0,7,2,2]

# 버블정렬
# result = []
# for i in range(len(my_list)-1,0,-1):
#     for j in range(i):
#         # left = my_list[j]
#         # right = my_list[j+1]

#         # print(left, right)
#         if my_list[j] > my_list[j+1]:
#             my_list[j], my_list[j+1] = my_list[j+1], my_list[j] #스왑

#             # temp = my_list[j]
#             # my_list[j] = my_list[j+1]
#             # my_list[j+1] = temp
# print(my_list)

# 카운팅정렬 -> 숫자가 커질수록 비효율적임
counter = [0 for i in range(10)]

for i in my_list:
    counter[i] += 1

# counter 결과 : [1, 1, 2, 1, 0, 0, 1, 1, 0, 1]
result = []

for value, count in enumerate(counter):  # enumerate : (인덱스, 값)
    for i in range(count):
        result.append(value)

print(result)


