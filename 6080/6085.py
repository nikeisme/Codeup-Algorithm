# w, h, b 가 공백을 두고 입력된다.
# 단, w, h는 모두 정수이고 1~1024 이다. b는 40이하의 4의 배수이다.

# 필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
# 단, 소수점 셋째 자리에서 반올림하여 둘째 자리까지 출력한다.

w,h,b = input().split()
res=int(w)*int(h)*int(b)/1024/1024/8

print('%.2f'%res,"MB")