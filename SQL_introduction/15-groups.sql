-- this is something: 
-- SELECT score FROM second_table WHERE score = (SELECT count(score) as number FROM second_table) ORDER BY score DESC;
SELECT score,COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
