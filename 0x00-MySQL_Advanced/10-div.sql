-- Create a function save div
DELIMITER //
CREATE FUNCTION SafeDiv(IN a INT, IN b INT)
RETURN FLOAT;
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a/b;
    END IF;
END //
DELIMITER ;