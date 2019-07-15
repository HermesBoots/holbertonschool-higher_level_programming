-- showing records that have names
SELECT score, name from second_table
WHERE name IS NOT NULL and name != ""
ORDER BY score DESC;
