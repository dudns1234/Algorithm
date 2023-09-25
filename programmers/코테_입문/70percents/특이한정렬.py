def solution(numlist, n):
    answer = []
    temp = [abs(i-n) for i in numlist]
    temp2 = [(i-n) for i in numlist]

    temp.sort()

    while len(temp):
        if temp.count(temp[0]) == 1:
            if temp[0] in temp2:
                answer.append(numlist[temp2.index(temp[0])])
                temp.pop(0)
            else:
                answer.append(numlist[temp2.index(-temp[0])])
                temp.pop(0)
        else:
            answer.append(numlist[temp2.index(temp[0])])
            answer.append(numlist[temp2.index(-temp[1])])
            temp.pop(1)
            temp.pop(0)

    return answer

print(solution([1,2,3,4,5,6],4))
print(solution([10000,20,36,47,40,6,10,7000],30))

