import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    Ci = list(map(int,input().split()))

    check = []
    pizza = []

    for j in range(1,M+1):
            check.append(j)

    for i in range(1,N+1):
        pizza.append(check.pop(0))
        pizza.append(Ci.pop(0))

    result = []

    while len(result) < M:
        
        for i in range(1,len(pizza),2):
            half = pizza[i] // 2
            if half != 0:
                pizza[i] = half
            else:
                if len(Ci) == 0:
                    
                    if pizza[i] != 0:
                        result.append(pizza[i-1])
                        pizza[i] = 0
            
                else:
                    result.append(pizza[i-1])
                    pizza[i-1] = check.pop(0)
                    pizza[i] = Ci.pop(0)
                    
        # if len(result) == M:
        #     break
        # else:
        #     continue

    print(f'#{tc} {result[-1]}')

# 강사님 풀이

for tc in range(1,T+1):
    # N:화덕의 크기
    # M:피자 개수
    N,M = list(map(int,input().split()))

    Ci = list(map(int,input().split()))

    # 피자에 번호를 부여하는 과정
    # 화덕에 들어가기전 피자 목록
    before = []
    for i in range(M):
        before.append([Ci[i],i])  # 피자에 넘버링

    # 화덕
    queue = [0] * N

    # 완성피자를 저장할 목록
    after = []

    # 완성피자가 구워야하는 피자 갯수랑 같아질때까지 반복
    while len(after) != M:

        # 화덕 입구에 공간이 비었으먄
        if queue[0] == 0:
            # 넣을 피자가 있으면
            if len(before) != 0:
                #남은 첫번째 치즈와 번호
                cheeze, idx = before.pop(0)
                # 화덕에 넣기
                queue.append([cheeze,idx])
                # 화덕 돌리기
                queue.pop(0)
            # 넣을 피자가 없을때
            else:
                queue.pop(0)
                queue.append(0)
        
        # 화덕 입구에 공간이 없으면 (이미 구워지고 있는 피자가 있는경우)
        else:
            # 치즈 절반 감소
            queue[0][0] //= 2

            # 치즈가 다 녹았는지 확인
            if queue[0][0] == 0:
                # 완성된 피자 꺼내기
                pizza = queue.pop(0)
                # 완성목록에 넣기
                after.append(pizza)

                if len(before) != 0:
                    # 남은 첫번째 치즈와 번호
                    cheeze, idx = before.pop(0)
                    # 화덕에 넣기
                    queue.append([cheeze, idx])
                else:
                    queue.append(0)
            
            # 아직 더 돌려야 하는경우
            else:
                queue.append(queue.pop(0))
    print(after)