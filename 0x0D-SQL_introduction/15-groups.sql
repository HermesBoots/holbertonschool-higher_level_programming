-- show the nmber of people with each score in the student table
SELECT score, count(*) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;
