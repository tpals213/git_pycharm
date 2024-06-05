# 파이썬 제어문 실행용 시작 스크립트

# 다른 파일에 있는 함수 사용하려면 import 선언
# import 디렉토리명.파일명
# import test_bool.operator_sample
# 파일이 제공하는 함수 사용시 디렉토리명.파일명.함수명(...)

# 모듈명이 길거나 복잡할 경우 줄임말 지정하고 사용 가능
# import 모듈명 as 줄임말
import test_bool.operator_sample as to
import conditional.ifSample as c
import conditional.ifMission1 as m1
import conditional.ifMission2 as m2
import conditional.ifMission3 as m3
import loop.forSample as fs
import loop.forMission1 as fm1
import loop.whileSample as ws

# 프로그램 시작하는 구문
if __name__ == '__main__':
    # 임포트한 파일에서 제공하는 함수 사용
    # 모듈명.함수명() 또는 줄임말.함수명
    # to.func_bool()
    # to.func_bool2()
    # to.func_compare()
    # to.func_logical()

    # 조건문 연습 if 문
    # c.test_if()
    # c.test_if2()
    # c.test_even()
    # c.test_even2()
    # c.test_range()
    # c.test_in()
    # c.checkPayment()
    # c.checkPayment2()
    # c.muli_if()
    # c.shortCondition()
    # c.shortCondition2()
    # m1.practice1()
    # m2.practice1()
    # m3.practice1()

    # 루프문 연습 for 문
    # fs.test_for1()
    # fs.sum()
    # fs.test_literable()
    # fs.test_range()
    # fs.for_indexing()
    # fs.print_gugudan()
    # fs.doubleFor()
    # fs.list_in_list()
    # fs.list_in_list2()
    # fm1.practice()

    # 루프문 연습 while 문
    ws.test_while()
    # ws.print_unicode()
    ws.print_unicode2()
