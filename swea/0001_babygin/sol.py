import sys
sys.stdin = open('input.txt')

T = int(input())  # 4개의 testcase

result = 0
numbers = []
for tc in range(1, T+1):
    numbers = input()
    counter = [0 for i in range(10)] # i는 안쓰기 때문에 [0 for _ in range(10)]도 가능
    
    for num in numbers:
        counter[int(num)] += 1

    idx = 0
    is_babygin = 0

    while idx < len(counter):
        # 1. triplet인지 검증
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1

        # 2. run인지 검증
        if idx < len(counter) - 2:
            if counter[idx] and counter[idx+1] and counter[idx+2] :
                is_babygin += 1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
        
        idx += 1
    if is_babygin == 2:
        print(f'#{tc} True')
    else:
        print(f'#{tc} False')