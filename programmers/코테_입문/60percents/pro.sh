# # 1. 폴더 선택
# echo '1. programmers 2. swea'
# read choice

# if [ $choice -eq 1 ]; then
#     site='programmers'
# elif [ $choice -eq 2 ]; then
#     site='swea'
# else
#     echo '1, 2를 입력해주세요'
#     exit 1
# fi

# 폴더이름 입력
echo '파일 이름을 입력해주세요'
read problem

# 폴더/파일 생성
touch -p "$problem.py"

cat << EOF > "$problem.py"
def solution



    return answer


print(solution())
print(solution())
print(solution())

EOF

echo "$problem.py 파일이 생성되었습니다."

# python selen.py "$problem"
