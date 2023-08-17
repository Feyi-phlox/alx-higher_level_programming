--  script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy (but the id can be different). Each record should display: tv_shows.title
SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN (
      SELECT tv_shows.id FROM tv_shows
      JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
      JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
      WHERE tv_genres.name = "Comedy" )
ORDER BY tv_shows.title ASC;
-- or the alias method
-- SELECT s.title
-- FROM tv_shows s
-- WHERE s.title NOT IN (
--      SELECT s.title
--      FROM tv_shows s
--      INNER JOIN tv_show_genres m ON s.id = m.show_id
--      INNER JOIN tv_genres g ON m.genre_id = g.id
--      WHERE g.name = 'Comedy'
-- )
-- ORDER BY s.title ASC;
