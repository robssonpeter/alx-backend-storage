-- Create a function save div
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
-- Use deterministic to suppress the binary logging error
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a/b;
    END IF;
END //
DELIMITER ;