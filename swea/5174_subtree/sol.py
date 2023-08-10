# Tree(이진트리 - 자식노드가 두!개!밖에 없다는게 특징)
import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def subtree(N):
        global count
        count += 1
        
        for i in temp[N]:
            if i:
                subtree(i)
        return count

for tc in range(1, T+1):
    E, N = map(int,input().split())
    nodes = list(map(int,input().split()))

    temp = [[] for _ in range(E+2)]
    for i in range(0,len(nodes),2):
        temp[nodes[i]].append(nodes[i+1])
    #print(temp)
    
    count = 0
    print(f'#{tc} {subtree(N)}')



# 강사님 풀이
# for tc in range(1, T+1):
#     # E : 간선의 개수
#     # N : 부모의 노드 / 시작노드
#     E, N = map(int,input().split())
#     nodes = list(map(int,input().split()))

#     left_node = [0] * (E+2)
#     right_node = [0] * (E+2)

#     for i in range(1,E*2,2):
#         parent = nodes[i]
#         child = nodes[i+1]

#         if left_node[parent] == 0:
#             left_node[parent] == child
        
#         else:
#             right_node[parent] == child

#     stack = [N]
#     count = 0

#     while stack:
#         now = stack.pop()
#         count += 1

#         if left_node[now]:
#             stack.append(left_node[now])
#         if right_node[now]:
#             stack.append(right_node[now])
#     print(count)