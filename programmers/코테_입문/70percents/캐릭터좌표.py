def solution(keyinput, board):
    answer = [0,0]
    # 'up' = [0,1]
    # 'down' = [0,-1]
    # 'left' = [-1,0]
    # 'right' = [1,0]
    up_down = board[1] // 2
    left_right = board[0] // 2

    for i in keyinput:
        if i == "left" and answer[0] > -left_right:
            answer[0] -= 1
        elif i == "right" and answer[0] < left_right:
            answer[0] += 1
        elif i == "up" and answer[1] < up_down:
            answer[1] += 1
        elif i == "down" and answer[1] > -up_down:
            answer[1] -= 1

    return answer

print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))
