di = {
    1 : "88",
    2 : "30",
    3 : "61",
    4 : "55",
    5 : "95"
}

for key, value in di.items():
    if int(value) >= 60:
        print(f'{key}번 학생은 {value}점으로 합격입니다.')
    else:
        print(f'{key}번 학생은 {value}점으로 불합격입니다.')

