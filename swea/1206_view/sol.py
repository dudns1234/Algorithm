import sys
sys.stdin = open('input.txt')

T = 10

# 내풀이
for tc in range(1, T+1):
    n = int(input())
    building = list(input().split())
    #print(n,building)
    count = 0
    for i in range(2,len(building)-1):
        max_list = []
        if int(building[i]) > int(building[i-1]) and int(building[i]) > int(building[i-2]) and int(building[i]) > int(building[i+1]) and int(building[i]) > int(building[i+2]):
            max_list.extend([int(building[i-1]),int(building[i-2]),int(building[i+1]),int(building[i+2])])
            #print(max_list)
            m = max(max_list)
            count += int(building[i]) - m

    print(f'#{tc} {count}')


# 강사님풀이
for tc in range(1, T+1):
    N = int(input())
    building_list = list(map(int,input().split()))
    total = 0

    for i in range(N):
        # print(i, building_list[i])
        now = building_list [i]
        
        # 현재 위치에 건물이 없다면 다음 건물로 이동
        if now == 0:
            continue

        # 나의 위치에 건물이 있는 경우
        else:
            # 양옆 * 2 건물의 높이를 비교
            dx = [-2,-1,1,2]  # delta = dx 내가 이동해야하는 칸수를 리스트 작성

            max_tall = 0

            for j in range(4):
                # i : 현재위치
                # dx : 기준건물을 중심으로 좌우 인덱스
                comp = building_list[i+dx[j]]

                if max_tall < comp :
                    max_tall = comp

            # 나머지 네개의 건물보다 내가 더 크다면 조망권 확보
            if now > max_tall:
                view = now - max_tall
                total += view


    