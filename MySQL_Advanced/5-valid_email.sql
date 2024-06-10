-- Create trigger to reset valid_email only when email is updated

CREATE TRIGGER reset_valid_email_trigger BEFORE UPDATE ON users
    FOR EACH ROW
        IF OLD.email != NEW.email THEN
            SET NEW.valid_email = 0;
        END IF;
