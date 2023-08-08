import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    cheese = list(map(int,input().split()))

    pizza = []
    temp2 = []
    for i in range(M):
        temp2.append(cheese[i])
    for i in range(N):
        temp = cheese.pop(0)
        pizza.append(temp)
        pizza.append(temp//2)

    # pizza : 3개 / cheese : 5개(원본)
    count = 1
    temp = []

    while len(pizza) > 2:
        count+=1
        #print(f'{count} 번 회전하였습니다.')
        for i in range(1,len(pizza),2):
            try:
                if len(pizza) > 2:
                    a = pizza[i] // 2
                    if a != 0:
                        pizza[i] = a
                    else:
                        if len(pizza) >= 2:
                            temp.append(pizza[i-1])
                            b = cheese.pop(0)
                            pizza[i-1] = b
                            pizza[i] = b
                else:
                    print(temp2.index(pizza[0])+1)
                    break
            except:
                pizza.pop(i)
                pizza.pop(i-1)

    # while len(cheese):
        
    #     count += 1 
    #     for i in range(len(pizza)):
    #         if pizza[i] != 0:
    #             pizza[i] = pizza[i] // 2
    #         else:
    #             pizza[i] = cheese.pop(0)
    #     print(pizza)


    # while cheese:  
        
    #     if len(cheese) >= N:
    #         temp = []
    #         temp.append(cheese.pop(0))
    #         temp.append(int(temp[0])//2)
        
    #         for i in temp:
    #             temp[1] = temp[1]//2
    #             if temp[1] == 0:
    #                 temp[0] = cheese.pop(0)
    #                 temp[1] = temp[0]
    #             else:
    #                 pass
    #     else:
    #         break

    #     print(temp)

        # for i in range(N):
        #     temp = []
        #     temp.append(cheese.pop(0))
        #     temp.append(int(temp[0])//2)
        #     count += 1

        #     if temp[1] == 0:
        #         temp[0].append(cheese.pop(0))
        #         temp[1].append(temp[0])
        #     else:
        #         pass

        
        #     print(temp)

    
        # data = cheese.pop(0)
        # cheese.append(data)

