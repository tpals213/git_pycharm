# path : model\\tour_model
# module : tour.tour_model
# 오라클 db에 TourInfo 객체 정보를 CRUD 처리하는 클래스 정의 스크립트

import common.dbConnectTemplate as db
import cx_Oracle as cx

class TourModel:
    # field
    __conn = ''

    # constructor
    def __init__(self):
        self.__conn = db.connect()

    # destructor
    # def __del__(self):
    #     try:
    #         if self.__conn != '':
    #             db.close(self.__conn)   # db 연결 해제
    #     except Exception as e:
    #         print('소멸자 오류 : ', e)

    # method
    # insert method
    def insert_tour(self, tp_tour):
        query = 'insert into tour values (:1, :2, :3, :4)'
        self.__conn = db.connect()
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.__conn.cursor() as cursor:
                cursor.execute(query, tp_tour)
            db.commit(self.__conn)
        except Exception as e:
            print('insert 오류 : ', e)
            db.rollback(self.__conn)
        finally:
            db.close(self.__conn)

    # delete all method
    def delete_all_tour(self):
        query = 'delete from tour'
        self.__conn = db.connect()
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.__conn.cursor() as cursor:
                cursor.execute(query)
            db.commit(self.__conn)
        except Exception as e:
            print('delete all 오류 : ', e)
            db.rollback(self.__conn)
        finally:
            db.close(self.__conn)

    # select all method
    def select_all_tour(self):
        query ='select * from tour order by rank'
        self.__conn = db.connect()
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.__conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            return result
        except Exception as e:
            print('select all 오류 : ', e)
        finally:
            db.close(self.__conn)

    # select one method
    def select_one_tour(self, tp_tour):
        query ='select * from tour where rank = :1'
        self.__conn = db.connect()
        try:
            # 자동 close 되게 처리 : with resource 문 이용
            with self.__conn.cursor() as cursor:
                cursor.execute(query, tp_tour)
                result = cursor.fetchone()
            return result
        except Exception as e:
            print('select 오류 : ', e)
        finally:
            db.close(self.__conn)

