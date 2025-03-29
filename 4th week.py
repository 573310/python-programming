a=int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계:"))
if a==1:
    b=input("*** 수식을 입력하세요:")
    print(b, "결과는",eval(b), "입니다.")
else:
    c=int(input("*** 첫 번째 숫자를 입력하세요: "))
    d=int(input("*** 두 번째 숫자를 입력하세요: "))
    total=sum(range(c,d+1))
    print(c,"+...+",d,total,"입니다.")