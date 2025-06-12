inFp = None
inStr = ""
Num = 1 

inFp = open("/Users/a573310/pythonprogramming/FileTest/python.txt", "r", encoding='UTF8')

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (Num, inStr), end="")
    Num += 1

inFp.close()
