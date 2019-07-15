-- showing records that have names
SELECT score, name from second_table
WHERE name != ""
ORDER BY score DESC;
