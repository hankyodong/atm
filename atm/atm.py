#잔액 초기화
balance= 1000
x=0
while True: #조건 결과가 True면 계속 작동합니다.
    
    num=input("사용하실 번호를 선택해주세요 (1.입금, 2.출금, 3.영수증보기, 4.종료):")

# 4를 입력하면 종료라는 출력메시지 print()
    if num== '4':
        print('종료')
        break
    