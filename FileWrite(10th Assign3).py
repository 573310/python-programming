import os

outFp = None
outStr = ""
fName = input("파일명을 입력하세요: ")

if os.path.exists(fName):
    print("파일이 이미 존재합니다. 내용을 출력합니다.\n")
    inFp = open(fName, "r", encoding='UTF8')
    inList = inFp.readlines()
    for inStr in inList:
        print(inStr, end="")
    inFp.close()
else:
    outFp = open(fName, "w", encoding='UTF8')
    while True:
        outStr = input("내용 입력 : ")
        if outStr != "":
            outFp.writelines(outStr + "\n")
        else:
            break
    outFp.close()
    print("--- 정상적으로 파일에 씀 ---")