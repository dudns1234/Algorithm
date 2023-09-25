def solution(id_pw, db):

    for i in db:
        id_pw_copy = id_pw.copy()
        for j in id_pw:
            if j not in i:
                pass
            else:
                id_pw_copy.remove(j)
                
    if len(id_pw_copy) == 0:
        return "login"
    elif len(id_pw_copy) == 1:
        return "wrong pw"
    else:
        return "fail"


print(solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"],[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"],[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))

