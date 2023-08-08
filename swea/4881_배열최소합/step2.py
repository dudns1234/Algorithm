# 모든 경우의 수를 탐색하는데 세로가 아닌

import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def search(idx, visited):

    if idx >= N:
        print(result)
        return # idx가 3이될때 idx(2)r로 남아있던 pop()을 진행시켜서 다시 재귀

    # 모든 경우의 수를 탐색하는 경우
    for i in range(N):   # idx = row, i = col
        if visited[i] == False:
            #print(idx, i,'=', series[idx][i])
            result.append(series[idx][i])
            visited[i] = True
            search(idx+1, visited)
            result.pop()  # idx = 3이 되면 그때 [1,2,3]에서 3을 pop하여 [1,2]로 만들고 다시 for문으로 돌게만듬
            visited[i] = False

for tc in range(1, T+1):
    N = int(input())
    
    series = []
    for _ in range(N):
        series.append(list(map(int,input().split())))

    result = []
    visited = [False] * N

    search(0, visited)