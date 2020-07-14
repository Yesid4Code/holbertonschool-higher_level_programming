-- Script that list all records with a specific score.
SELECT score, name FROM second_table WHERE (score >= 10) ORDER by score desc;
