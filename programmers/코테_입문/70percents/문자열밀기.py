def solution(A, B):

    a = [i for i in A]
    b = [i for i in B]

    count = 0
    for _ in range(len(a)):
        if a == b:
            return 0
        else:
            a.insert(0,a[-1])
            a.pop(-1)
            count += 1
            if a == b:
                return count
            else:
                continue
    return -1


print(solution("hello","ohell"))
print(solution("apple","elppa"))
print(solution("atat","tata"))
print(solution("abc","abc"))

