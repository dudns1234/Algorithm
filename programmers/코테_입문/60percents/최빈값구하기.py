def solution(array):

    temp = list(set(array))
    temp2 = []

    for i in temp:
        temp2.append(array.count(i))

    if len(temp2) >= 2:
        if temp2.count(max(temp2)) == 1:
            if max(temp2)!= min(temp2):
                a = temp2.index(max(temp2))
                return temp[a]
            elif max(temp2) == min(temp2):
                return -1
        elif temp2.count(max(temp2)) >= 2:
            return -1
    else:
        return array[0]


print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1, 1, 1]))
print(solution([1, 1, 2, 2, 3]))



    # for j in temp:
    #     # print(j, array.count(j))
    #     # print("--")
    #     if array.count(j) > 2:
    #         if answer <= array.count(j):
    #             answer = array.count(j)
    #         else:
    #             pass
    #     elif array.count(j) == 2:

    #     else:
    #         if answer > array.count(j):
    #             pass
    #         else:
    #             answer = array.count(j)
    # return answer
