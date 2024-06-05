-- dbscript\\table.sql
-- 동적 웹 크롤링에서 여행지 검색 결과 저장용 테이블 생성 스크립트

-- drop table tour cascade constraints;

create table tour (
    rank varchar2(100),
    name varchar2(100),
    description varchar2(1000),
    category varchar2(100)
)
/
commit;