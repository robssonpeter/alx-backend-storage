-- Index idx_name_first_score on the table 
-- and the first letter of name and the score
USE holberton;
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score)