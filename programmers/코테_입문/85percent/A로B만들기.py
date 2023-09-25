def solution(before, after):
    answer = 0
    for i in before:
        if i in after:
            after = after.replace(i,"",1)
        else:
            return 0
    if len(after) >= 1:
        return 0
    return 1


print(solution("olleh","hello"))
print(solution("allpe","apple"))

# 다른 풀이
def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0
