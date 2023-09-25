def solution(n):
    temp = 1
    three_x = []
    
    while True:

        if temp % 3 == 0 or str(temp).count('3') >= 1:
            temp += 1
        else:
            three_x.append(temp)
            temp += 1
        
        if len(three_x) == n:
            return three_x[-1]

print(solution(15))
print(solution(40))