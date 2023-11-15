-- Lists the number od records with the same score in the table second_table
-- hbtn_0c_0 and displays the score and number of records for this score 
-- with the label number
SELECT score, COUNT(*) AS number FROM second_table 
GROUP BY score ORDER BY score DESC;
