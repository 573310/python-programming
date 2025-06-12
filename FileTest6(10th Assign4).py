inFp, outFp = None, None
inStr = ""

inName = input("소스 파일명을 입력하세요: ")
outName = input("타깃 파일명을 입력하세요: ")

inFp = open(inName, "r")
outFp = open(outName, "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()

print("--- %s 파일이 %s 파일로 복사되었음 ---" % (inName, outName))