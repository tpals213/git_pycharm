-- 크롤링 데이터 저장용 테이블 생성 스크립트
-- table.sql
-- 네이버 영화 상영 정보 제공 페이지 크롤링 결과 저장용 테이블
-- 테이블명 : movie
-- 파이썬의 Movie 클래스 필드명과 테이블 컬럼명 일치시킴 => 필드명의 '__' 제외함
-- rank : pk, 나머지 컬럼은 not null
-- 컬럼 comment 도 지정
-- 컬럼명 : 영화명, 상영날짜, 감독, 배우, 장르, 평점, 관람등급
-- https://movie.naver.com/movie/running/current.nhn

-- 1. 테이블 생성
-- drop table movie cascade constraints;

create table movie (
    rank number constraint PK_MOVIE primary key,
    title varchar2(100) not null,
    star_point number(7, 2) not null ,
    release_date varchar2(100),
    genre varchar2(30) not null,
    link varchar2(2000)
);

comment on column movie.rank is '상영순위';
comment on column movie.title is '영화제목';
comment on column movie.star_point is '영화별점';
comment on column movie.release_date is '개봉일';
comment on column movie.genre is '장르';
comment on column movie.link is '상세페이지 URL';

commit;