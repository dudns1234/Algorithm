def solution(s):
    answer = []

    for i in s:
        if s.count(i) == 1:
            answer.append(i)

    answer.sort()

    return ''.join(answer)


print(solution("abcabcadc"))
print(solution("abdc"))
print(solution("hello"))

# list conprehension
def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer