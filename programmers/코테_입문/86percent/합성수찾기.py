def solution(n):
    result = []
    temp = [i for i in range(2,n+1)]
    #print(temp)
    for i in range(4,n+1):
        for j in range(2,(n//2)+1):
            if i*j in temp:
                if i*j not in result:
                    result.append(i*j)
                    print(result)
            else:
                pass

    return len(result)


print(solution(10))
print(solution(15))


# 다른 풀이
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output
