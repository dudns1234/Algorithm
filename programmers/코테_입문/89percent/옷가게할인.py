def solution(price):
    if price >= 100000 and price < 300000:
        return int(price - (price * 0.05))
    elif price >= 300000 and price < 500000:
        return int(price - (price * 0.1))
    elif price>=500000:
        return int(price - (price * 0.2))
    else:
        return int(price)
    
print(solution(150000))
print(solution(580000))

#다른 풀이

def solution(price):
    if price>=500000:
        price = price *0.8
    elif price>=300000:
        price = price *0.9
    elif price>=100000:
        price = price * 0.95
    return int(price)