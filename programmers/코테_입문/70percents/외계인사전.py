def solution(spell, dic):
    
    for i in dic:
        spell2 = spell.copy()
        for j in spell:
            if j not in i:
                pass
            else:
                spell2.remove(j)
                if len(spell2) == 0:
                    return 1
                else:
                    continue
    return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))



