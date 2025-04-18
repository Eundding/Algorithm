SELECT DISTINCT U.USER_ID,  U.NICKNAME, CONCAT_WS(' ', CITY, STREET_ADDRESS1, STREET_ADDRESS2) AS '전체주소', 
    CONCAT_WS('-', SUBSTRING(TLNO, 1, 3), SUBSTRING(TLNO, 4, 4), SUBSTRING(TLNO, 8, 4)) AS '전화번호'
FROM USED_GOODS_USER U
    INNER JOIN USED_GOODS_BOARD B ON B.WRITER_ID = U.USER_ID
WHERE U.USER_ID IN (SELECT WRITER_ID 
        FROM USED_GOODS_BOARD
        GROUP BY WRITER_ID
        HAVING COUNT(*) >= 3) 
        
ORDER BY U.USER_ID DESC;