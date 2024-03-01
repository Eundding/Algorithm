SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
# WHERE SKILL_1 = 'Python' or SKILL_2 = 'Python' or SKILL_3 = 'Python' 
WHERE 'Python' IN (SKILL_1, SKILL_2, SKILL_3)
ORDER BY 1;