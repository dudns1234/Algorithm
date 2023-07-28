# example1
blood_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

blood_dict = {
    'A' : 0,
    'B' : 0,
    'AB' : 0,
    'O' : 0
}

for blood in blood_list:
    blood_dict[blood] += 1

print(blood_dict)

# example2
## if blood_dict처럼 A,B,AB,O까지만 있을 때는 괜찮지만 list에 더 추가가된다면?
location_list = ['서울', '부산', '서울', '서울', '대전', '제주', '광주', '부산','LA']
location_dict = {}

for location in location_list:
    # 이미 기록을 한 경우
    if location in location_dict.keys():
        location_dict[location] += 1
    # 처음 등장한 경우
    else:
        location_dict[location] = 1

print(location_dict)