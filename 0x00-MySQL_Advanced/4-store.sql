-- Create a trigger to change quantity after order placement
DELIMITER //
CREATE TRIGGER decrement_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items SET quantity = quantity - NEW.number 
    WHERE items.name = NEW.item_name;
END //
DELIMITER ;