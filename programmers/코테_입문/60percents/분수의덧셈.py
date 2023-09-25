def solution(numer1, denom1, numer2, denom2):
    answer = []

    if denom1 < denom2:
        if denom2 % denom1 == 0:
            a = denom2 // denom1
            child = numer1 * a
            if child % denom2 == 0:
                answer.append(denom2//(child+numer2))
                answer.append(1)
            else:
                
                answer.append(child+numer2)
                answer.append(denom2)
        else:
            a = denom1 * denom2
            b = numer1 * denom2
            c = numer2 * denom1
            if a % (b+c) == 0:
                answer.append(a//(b+c))
                answer.append(1)
            else:
                answer.append(b+c)
                answer.append(a)
    elif denom1 > denom1:
        if denom1 % denom2 == 0:
            a = denom1 // denom2
            child = numer2 * a
            if child % denom1 == 0:
                answer.append(denom1//(child+numer1))
                answer.append(1)
            else:
                answer.append(child+numer1)
                answer.append(denom1)
        else:
            a = denom1 * denom2
            b = numer1 * denom2
            c = numer2 * denom1
            if a % (b+c) == 0:
                answer.append(a//(b+c))
                answer.append(1)
            else:
                answer.append(b+c)
                answer.append(a)
    else:
        a = numer1 + numer2
        if a % denom1 == 0:
            answer.append(a // denom1)
            answer.append(1)
        else:
            answer.append(a)
            answer.append(denom1)

    return answer

print(solution(1,2,3,4))
print(solution(9,2,1,3))
print(solution(999,999,999,999))

    # if denom2 % denom1 == 0 or denom1 % denom2 == 0:
    #     if denom2 > denom1:
    #         a = denom2 // denom1
    #         child = numer1 * a
    #         if denom2 % child == 0:
    #             answer.append(child // denom2)
    #             answer.append(1)
    #         else:
    #             answer.append(child+numer2)
    #             answer.append(denom2)
    #     if denom1 > denom2 :
    #         a = denom1 // denom2
    #         child = numer2 * a
    #         if denom1 % child == 0:
    #             answer.append(child // denom1)
    #             answer.append(1)
    #         else:
    #             answer.append(child+numer1)
    #             answer.append(denom1)
    # else:
    #     parent = denom1 * denom2
    #     child1 = numer1 * denom2
    #     child2 = numer2 * denom1
    #     answer.append(child1+child2)
    #     answer.append(parent)
    
    # return answer
    # if denom2 > denom1:
    #     if denom2 % denom1 == 0 :
    #         a = denom2 // denom1
    #         child = numer1 * a
    #         answer.append(child+numer2)
    #         answer.append(denom2)
    #     else:
    #         parent : denom1 * denom2
    #         child1 : numer1 * denom2
    #         child2 : numer2 * denom1
    #         answer.append(child1+child2)
    #         answer.append(parent)
    # else:
    #     if denom1 % denom2 == 0 :
    #         a = denom2 // denom1
    #         child = numer1 * a
    #         answer.append(child+numer2)
    #         answer.append(denom2)
    #     else:
    #         parent : denom1 * denom2
    #         child1 : numer1 * denom2
    #         child2 : numer2 * denom1
    #         answer.append(child1+child2)
    #         answer.append(parent)
    # return answer

    # if denom2 % denom1 == 0 :
    #     if denom2 > denom1:
    #         a = denom2 // denom1
    #         child = numer1 * a
    #         answer.append(child+numer2)
    #         answer.append(denom2)
    #     if denom1 > denom2 :
    #         a = denom1 // denom2
    #         child = numer2 * a
    #         answer.append(child+numer1)
    #         answer.append(denom1)
    # else:
    #     parent : denom1 * denom2
    #     child1 : numer1 * denom2
    #     child2 : numer2 * denom1
    #     answer.append(child1+child2)
    #     answer.append(parent)
        

    # return answer


