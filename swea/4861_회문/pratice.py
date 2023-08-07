import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1,T+1):
    N, M = map(int,input().split())
    char = []
    for _ in range(N):
        char.append(list(map(str,input())))
    # print(char)

    result = []
    for row in range(N):
        for col in range(N):
            front = char[row][col]
            back = char[row][len(char[row])-col-1]
            #print(front,back)
            if len(char[row]) == M:
                if front == back:
                    result.append(front)
                    continue
                else:
                    break
            elif len(char[row]) > M:
                if front == back:
                    result.append(front)
                    #print(result)
                    continue
                elif char[row][0] != char[row][len(char[row])-1]:
                    char[row].remove(char[row][0])
                    #print(char[row])
                    continue
                else:
                    break
    print(result)

    # 0 -- 19 : K -- N 
    # 1 -- 19 : S -- N
    # 2 -- 19 : N -- N
    # 3 -- 18 : S -- S
    # 4 -- 17
    # result = []
    # for i in char:
    #     print(i)
    #     for j in range(M):
    #         if i[j] == i[len(i)-j-1]:
    #             #print(char[j])
    #             result.append(i[j])
    #             continue 
    #         else:
    #             break
    
    # result2 = []
    # for m in range(len(char)):
    #     for n in range(M):
    #         if char[n][m]==char[len(char)-n-1][m]:
    #             result2.append(char[n][m])
    #             continue
    #         else:
    #             break
    # print(result2)


#[['G', 'O', 'F', 'F', 'A', 'K', 'W', 'F', 'S', 'M'], 
# ['O', 'Y', 'E', 'C', 'R', 'S', 'L', 'D', 'L', 'Q'],
# ['U', 'J', 'A', 'J', 'Q', 'V', 'S', 'Y', 'Y', 'C'],
# ['J', 'A', 'E', 'Z', 'N', 'N', 'Z', 'E', 'A', 'J'],
# ['W', 'J', 'A', 'K', 'C', 'G', 'S', 'G', 'C', 'F'],
# ['Q', 'K', 'U', 'D', 'G', 'A', 'T', 'D', 'Q', 'L'],
# ['O', 'K', 'G', 'P', 'F', 'P', 'Y', 'R', 'K', 'Q'],
# ['T', 'D', 'C', 'X', 'B', 'M', 'Q', 'T', 'I', 'O'],
# ['U', 'N', 'A', 'D', 'R', 'P', 'N', 'E', 'T', 'Z'],
# ['Z', 'A', 'T', 'W', 'D', 'E', 'K', 'D', 'Q', 'F']]