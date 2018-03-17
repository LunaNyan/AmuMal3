#!/usr/bin/python3

from datetime import datetime

print ("아무말3 for Python3 Alpha001")
print ("by 루냥이, at 20180318, Twitter @ItsLunaNyan")
print (" ")

logr = open("amumal.txt", "r")

if logr.read(8) == "":
    print ("이 프로그램은 타임라인 방식으로 메모를 기록하는 프로그램입니다.")
    print ("간단히 메모할 내용을 입력하고 Enter을 눌러 기록합니다.")
    print (" ")
    print ("메모할 내용 대신 원하는 명령어를 입력하면 동작이 수행됩니다.")
    print ("명령어에 대한 자세한 내용이 필요하면 help를 입력하세요.")
    print (" ")

while 1:
    inp = input("입력 : ")
    if inp == "exit":
        break
    elif inp == "help":
        print ("이 프로그램은 타임라인 방식으로 메모를 기록하는 프로그램입니다.")
        print ("간단히 메모할 내용을 입력하고 Enter을 눌러 기록합니다.")
        print (" ")
        print ("메모할 내용 대신 원하는 명령어를 입력하면 동작이 수행됩니다.")
        try:
            input("계속하려면 Enter 키를 눌러주세요.")
        except SyntaxError:
            pass
        print ("명령어와 동작은 다음과 같습니다.")
        print (" ")
        print ("exit        프로그램이 종료됩니다.")
        print (" ")
        print ("자세한 정보는 알 게 뭐야")
    else:
        logf = open("amumal.txt", "a")
        logf.write(inp + "\n" + str(datetime.now()) + "\n----------\n")
        logf.close()
