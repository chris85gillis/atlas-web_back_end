-- Trigger to decrease the quantity


CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
    FOR EACH ROW UPDATE items
        SET items.quantity = items.quantity - NEW.number
        WHERE items.name = NEW.item_name;
