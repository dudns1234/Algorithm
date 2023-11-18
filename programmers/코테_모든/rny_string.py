def solution(rny_string):
    return rny_string.replace('m','rn')  


# replace 함수
# 변수.replace(old,new,[count])

# - old : 현재 문자열에서 변경하고 싶은 문자
# - new: 새로 바꿀 문자
# - count: 변경할 횟수. 횟수는 입력하지 않으면 old의 문자열 전체를 변경한다. 기본값은 전체를 의미하는 count=-1로 지정되어있다. 