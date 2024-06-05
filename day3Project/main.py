# test_dict 디렉토리 안에 있는 dict_sample.py 파일 안의 함수를 사용하려면
# import 문을 사용해서 임포트 선어해야 함

# 모듈 : 함수를 가지고 있는 파이썬 파일
# import 파일명 => 같은 디렉토리 안의 파일을 불러 들일 때
# import 디렉토리명.파일명 => 다른 디렉토리 안의 파일을 불러 들일 때

# import test_dict.dict_sample
# 모듈명이 길거나 복잡하면 줄임말을 지정할 수 있음
# import 모듈명 as 줄임말
import test_dict.dict_sample as ts
import mission.dict_mission1 as ms1
import mission.dict_mission2 as ms2
import test_set.set_sample as ss

if __name__ == '__main__':
   # 임포트한 모듈(파일)이 가진 함수를 사용하려면 (함수 실행)
    # 모듈명.함수명() 또는 모듈줄임말.함수명()
    #test_dict.dict_sample.test1()
    # ts.test1()
    # ts.test2()
    # ts.test3()
    # ts.test4()
    # ts.test5()
    # ts.test6()
    # ts.test7()
    # ts.test8()

    # 사전 자료형 복습문제 1
    # ms1.dict_func()

    # 사전 자료형 복습문제 2
    ##ms2.dict_mission2()

    # set 자료형 테스트
    ss.test1()
    ss.test2()
    ss.test3()
    ss.test4()
    ss.test5()
    ss.test6()
    ss.test7()