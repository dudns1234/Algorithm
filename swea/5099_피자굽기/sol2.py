import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    cheese = list(map(int,input().split()))

    check = []
    pizza = []

    for j in range(1,M+1):
            check.append(j)

    for i in range(1,N+1):
        pizza.append(check.pop(0))
        pizza.append(cheese.pop(0))

    temp = []

    while True:
        
        for i in range(1,len(pizza),2):
            a = pizza[i] // 2
            if a != 0:
                pizza[i] = a
            else:
                if len(cheese) == 0:
                    
                    if pizza[i] != 0:
                        temp.append(pizza[i-1])
                        pizza[i] = 0
            
                else:
                    temp.append(pizza[i-1])
                    pizza[i-1] = check.pop(0)
                    pizza[i] = cheese.pop(0)
                    
        if len(temp) == M:
            break
        else:
            continue

    print(f'#{tc} {temp[-1]}')
