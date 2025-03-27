input_a=int(input("입력 진수 결정(2/8/10/16) : "))
var=input("값 입력 : ")

if input_a==2:
    var10=int(var,2)
if input_a==8:
    var10=int(var,8)
if input_a==10:
    var10=int(var,10)
if input_a==16:
    var10=int(var,16)
    
print("2진수 ==> ", bin(var10))
print("8진수 ==> ", oct(var10))
print("10진수 ==> ", var10)
print("16진수 ==> ", hex(var10))