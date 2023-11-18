def solution(arr, k):
    answer = []
    if k % 2 == 1:
        for i in arr:
            answer.append(i*k)
    else:
        for i in arr:
            answer.append(i+k)
    return answer


# 홀수 구하는 방법은 무조건 "특정값 % 2 == 1"
# 짝수 구하는 방법은 무조건 "특정값 % 2 == 0"