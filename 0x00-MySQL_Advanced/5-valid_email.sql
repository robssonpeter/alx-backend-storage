-- Validate an email when use changes it
DELIMITER //
CREATE TRIGGER validate_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        UPDATE users 
        SET valid_email = 0 
        where id = OLD.id;
    END IF;
END //
DELIMITER ;