def solution(chicken):

    free_chicken = chicken // 10  # 199
    free = chicken // 10
    coupon = chicken % 10  # 9
    plus_coupon = coupon + free_chicken  # 208

    while True:

        if plus_coupon >= 10:
            free += plus_coupon // 10 # 20
            free_chicken = plus_coupon // 10
            coupon = plus_coupon % 10
            plus_coupon = coupon + free_chicken

        else:
            return free

print(solution(100))
print(solution(1081))
print(solution(1999))  # 222

# 다른 사람 풀이

def solution(chicken):
    coupon = chicken
    answer = 0
    while coupon >= 10:
        answer += coupon // 10
        coupon = coupon % 10 + coupon // 10
    return answer