# n = 먹는사람
# 한 판당 7조각

def solution(n):
    if n % 7 == 0:
        return int(n/7)
    else:
        return int((n/7) + 1)

print(solution(7))
print(solution(1))
print(solution(15))