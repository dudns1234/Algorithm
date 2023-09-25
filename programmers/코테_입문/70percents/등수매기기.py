def solution(score):
    answer = [sum(i)/2 for i in score]

    answer_copy = answer.copy()
    answer_copy = list(set(answer_copy))
    answer_copy.sort(reverse=True)
    answer_copy2 = answer.copy()
    
    a = 0

    for j in answer_copy:
        a += 1      
        if answer.count(j) == 1:  
            answer_copy2[answer.index(j)] = a  
        else:
            num = -1  
            for _ in range(1,answer.count(j)+1): 
                answer_copy2[answer.index(j)] = a
                num += 1
            a += num

    return answer_copy2


print(solution([[1,1], [2,1], [3,1], [4,1], [5,1], [6,1], [7,1], [8,1], [9,1], [0,0]]))
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))

# 다른 사람 풀이
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

