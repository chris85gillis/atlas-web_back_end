-- This procedure takes a user_id, a project name, and a score, and adds a new correction to the corrections table. If the project does not exist, it creates a new project with the given name.


DELIMITER //
CREATE PROCEDURE AddBonus(IN p_user_id INT, IN p_project_name VARCHAR(255), IN p_score INT)
BEGIN
    DECLARE v_project_id INT;

    -- Check if project exists
    SELECT id INTO v_project_id FROM projects WHERE name = p_project_name;

    -- If not, create it
    IF ISNULL(v_project_id) THEN
        INSERT INTO projects (name) VALUES (p_project_name);
        SET v_project_id := LAST_INSERT_ID();
    END IF;

    -- Insert the new correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (p_user_id, v_project_id, p_score);
END //
DELIMITER ;
