-- The script that creates a index based
-- on the first letter of a column
CREATE INDEX idx_name_first
ON names (LEFT(`name`, 1));