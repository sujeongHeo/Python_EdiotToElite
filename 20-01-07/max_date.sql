<!-- 문제-->
<!-- 가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요. -->

<!-- 방법1 --> 
SELECT MAX(DATETIME) FROM ANIMAL_INS
<!-- 방법2 -->
SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME DESC LIMIT 1

<!-- 느낀 점 -->
<!-- 솔직히 바로 검색해서 답부터 보았다. -->
<!-- 날짜의 숫자가 큰 게 최신 이니까 SELECT MAX(DATETIME)이라고 쓰인 게 인상적이다 -->
<!--  ORDER BY 는 기본적으로 오름차순인데 뒤에 DESC 로 내림차순 해주고 맨 위 첫 번째를 가져온 게 인상적 -->
