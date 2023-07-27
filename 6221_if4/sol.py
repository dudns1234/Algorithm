import sys
sys.stdin = open('input.txt', encoding='UTF8')

Man1 = input() # 바위
Man2 = input() # 가위

# if Man1 == "바위" and Man2 =="가위":
#     print("Result : Man1 Win!")
# elif Man1 == "바위" and Man2 =="바위":
#     print("Result : Draw")
# elif Man1 == "바위" and Man2 =="보":
#     print("Result : Man2 Win!")

# 가위, 바위, 보
#   0 ,  1  , 2

#보, (가위)     win2    2   : 2는 win2
#(바위), 가위   win1    1   : 1은 win1
#(보), 바위     win1    1   : 1은 win1
#가위, (바위)   win2    -1  : -1은 win2
#바위, (보)     win2    -1  : -1은 win2
#(가위), 보     win1    -2  : -2은 win1

rcp = ['가위','바위','보']

man1_idx = rcp.index(Man1)
man2_idx = rcp.index(Man2)

print(man1_idx,man2_idx)

result = man1_idx - man2_idx

if result == 0:
    print("Result : Man2 Win!")
elif result > 0 :
    print(f"Result : Man{result} Win!")
else:
    if result == -1:
        print("Result : Man2 Win!")
    else:
        print("Result : Man1 Win!")