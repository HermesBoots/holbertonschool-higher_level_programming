-- get records in one table that match to another without using JOIN
SELECT `id`, `name` FROM `cities` WHERE `state_id` IN (
	SELECT `id` FROM `states` WHERE `name` = "California"
) ORDER BY `id` ASC;
