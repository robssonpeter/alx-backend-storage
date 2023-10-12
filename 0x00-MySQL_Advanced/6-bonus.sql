-- Store Procedure for Adding bonus
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name TEXT, IN score FLOAT)
BEGIN
    