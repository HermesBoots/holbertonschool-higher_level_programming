-- list alll shows and the different genres they're a part of, even if the
-- show has no genre
SELECT `tv_shows`.`title`, `tv_show_genres`.`genre_id`
FROM `tv_show_genres` RIGHT OUTER JOIN `tv_shows`
ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
ORDER BY `tv_shows`.`title`, `tv_show_genres`.`genre_id`;
