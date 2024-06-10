-- A safe division function that returns 0 if the second argument is 0

DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //
DELIMITER ;
