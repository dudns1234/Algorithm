# for문으로 누적곱 연산
def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        answer = 0
        for i in range(len(num_list)):
            if i == 0:
                answer = num_list[i]
            else:
                answer = answer*num_list[i]
        return answer


# math 라이브러리의 prod함수로 연산 (누적곱 리턴)
from math import prod 
def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return prod(num_list)