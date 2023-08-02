import sys

sys.stdin = open('input.txt')

T = int(input())

# N번 정류장
# 한번 충전으로 최대한 이동할 수 있는 정류장 수 K
# 충전기가 설치된 M개의 정류장 번호
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력

# k = 3 n = 10 m = 5
# 1 3 5 7 9


for tc in range(1, T+1): 
    k,n,m= map(int,input().split())  # k = 3 n = 10 m = 5
    numbers = list(map(int,input().split())) # 1 3 5 7 9
    yj = 0
    count = 0
    #print(k,n,m,numbers)
    while yj < n:
        for i in range(0,n+1,k):
            if i == '0':
                pass
            if int(i) in numbers:
                count +=1
                yj = i
            else:
                pass
                no_count = 0
                for j in range(i-1,k,-1):
                    if int(j) in numbers:
                        count +=1
                        yj = j
                    else:
                        no_count +=1
                    if no_count >= k-1:
                        print("0")
                        break
    # print(f'#{tc} {count}')                    


# result = 0
# um = 0

# for tc in range(1, T+1):
#     N = input()
#     #print(N)
#     knm = list(map(int,N.split())) # K, N, M
#     numbers = list(map(int,input().split()))
#     counter = [0 for i in range(knm[1]+1)]
#     for i in range(int(knm[1])+1):
#         for j in numbers:
#             if i == j:
#                 counter[i]+=1
#     #print(counter)
#     for m in range(0,len(counter)+1,int(knm[0])):
#         # 0부터 시작해야해서 0은 제외
#         if m == 0:
#             pass
#         # 1인 경우 count
#         elif counter[int(m)] == 1:
#             result +=1
#         # 0인 경우 
#         elif counter[int(m)] == 0:  # m=6
#             li = []
#             # 온만큼 그전에 충전소가 있는지 확인
#             for k in range(1,knm[0]): 
#                 li.append(counter[int(m)-int(k)])    
#             # 리스트에 충전소가 1개라도 있다면 result+1
#             if 1 in li:
#                 result += 1
#             # 충전소가 없었다면 끝
#             else:
#                 result = 0
#                 break
#     print(f'#{tc} {result}')


# # 강사님 풀이

# for tc in range(1, T+1):
#     K, N, M = map(int,input().split())
#     # K : 최대로 이동 가능한 정류장 수
#     # N : 종점
#     # M : 충전기가 설치된 정류장 수
#     bus_stop = list(map(int, input().split()))
    
#     count = 0
#     now = 0

#     if K > N:
#         count = 0
#     else:
#         while now < N:
#             # 현재 위치 (now)에서 최대로 갈 수 있는 범위를 찾는다.
#             # 최대로 갈 수 있는 범위(now+K) 부터 현재 위치까지 반복
#             for i in range(now+K, now, -1): #3,0,-1
#                 # 1. 최대범위가 종점을 넘는경우
#                 if i >= N:
#                     now = N
#                 # 2. 최대범위가 종점을 아직 넘지 않은 경우
#                 if i in bus_stop:
#                     # 가장 뒤에 있는 충전소로 이동
#                     now = i

#                     # 충전을 하고 이동을 했으니 카운트 증가
#                     count += 1

#                     # 마지막 충전소를 찾았으니 더이상 후진할 필요 없음
#                     break
#                 else:
#                     count = 0
#                     now = N

#     print(f'#{tc} {count}')