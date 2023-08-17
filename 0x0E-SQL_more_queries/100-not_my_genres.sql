-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different).Each record should display: tv_genres.name
SELECT name FROM tv_genres
WHERE tv_genres.id NOT IN (
      SELECT tv_genres.id FROM tv_genres
      JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
      JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
      WHERE tv_shows.title = "DEXTER" )
ORDER BY tv_genres.name ASC;
-- or the alias method
-- SELECT g.name
-- FROM tv_genres g
-- WHERE g.name NOT IN (
--      SELECT g.name
--      FROM tv_genres g
--      INNER JOIN tv_show_genres m ON g.id = m.genre_id
--      INNER JOIN tv_shows s ON m.show_id = s.id
--       WHERE s.title = 'Dexter'
-- )
-- ORDER BY g.name ASC;
