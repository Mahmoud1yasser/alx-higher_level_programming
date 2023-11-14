-- script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT score, name FROM second_table
ORDER BY score DESC;
DELETE FROM second_table
WHERE score <= 5;
