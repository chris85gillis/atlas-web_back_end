-- This trigger resets the 'valid_email' field to 0 when the 'email' field is updated.
-- This is useful when we want to reset the validation status of an email address.
-- For example, if a user resets their password, we want to reset the 'valid_email' field.


DELIMITER $$
CREATE TRIGGER reset_valid_email_trigger BEFORE UPDATE ON users
    FOR EACH ROW
        IF OLD.email != NEW.email THEN
            SET NEW.valid_email = 0;
        END IF;
    END $$
DELIMITER ;
