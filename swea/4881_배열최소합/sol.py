import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def search(idx, visited, SUM):
    global MIN_SUM  # MIN_SUM이 전역번수이기 때문에 global로 데려옴
    if idx >= N:
        if SUM < MIN_SUM:
            MIN_SUM = SUM
        print(result,sum(result))
        return # idx가 3이될때 idx(2)r로 남아있던 pop()을 진행시켜서 다시 재귀
    
    if SUM > MIN_SUM:  # 반복횟수 줄어듬 (애초에 진행하다가 MIN_SUM보다 큰 경우가 나오면 진행조차 안해도되기 때문) 가지치기!
        return

    # 모든 경우의 수를 탐색하는 경우
    for i in range(N):   # idx = row, i = col
        if visited[i] == False:
            #print(idx, i,'=', series[idx][i])
            #result.append(series[idx][i])
            SUM += series[idx][i]
            visited[i] = True
            search(idx+1, visited, SUM)
            result.pop()  # idx = 3이 되면 그때 [1,2,3]에서 3을 pop하여 [1,2]로 만들고 다시 for문으로 돌게만듬
            SUM -= series[idx][i]
            visited[i] = False

for tc in range(1, T+1):
    N = int(input())
    
    series = []
    for _ in range(N):
        series.append(list(map(int,input().split())))

    result = []
    visited = [False] * N

    SUM = 0 # 각 리스트 결과물 (각 리스트 더한 것을 넣기 위함)
    MIN_SUM = 10000000  # 최종결과물

    search(0, visited, SUM)
