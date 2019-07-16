-- joining a TV show ID with its rating and adding them together
SELECT `tv_shows`.`title`, sum(`tv_show_ratings`.`rate`) AS "rating"
FROM `tv_shows`
INNER JOIN `tv_show_ratings` ON `tv_shows`.`id` = `tv_show_ratings`.`show_id`
GROUP BY `tv_shows`.`title`
ORDER BY `rating` DESC;
