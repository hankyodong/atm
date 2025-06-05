#잔액 초기화
balance= 1000
x=0
while True: #조건 결과가 True면 계속 작동합니다.
    
    num=input("사용하실 번호를 선택해주세요 (1.입금, 2.출금, 3.영수증보기, 4.종료):")

# 4를 입력하면 종료라는 출력메시지 print()
    if num== "1":
        #얼마를 입금할거야?
        deposit_amount = int(input("입금할 금액을 입력해주세요:"))
        #balance
        balance += deposit_amount #balance= balance + deposit_amount
        
        print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}입니다.')
    
    if num== '4':
        print('종료')
        break
    