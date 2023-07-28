# def solution(n, k):
#     if n >= 10:
#         answer = 12000 * n + 2000 * k - n//10 * 2000
#         return answer
#     else:
#         answer = 12000 * n + 2000 * k - k * 2000
#         return answer

# print(format(solution(10,3),','))
# print(format(solution(64,6),','))

def solution(n, k):
    # n => 양꼬치 n인분
    # k => 음료수 k개
    answer = 0
    service = n // 10

    answer = (12000 * n) + (k-service) * 2000

    return answer

print(format(solution(10,3),','))
print(format(solution(64,6),','))