-- This script adds a procedure to add a bonus to a project that a user has contributed to.
-- The procedure takes three parameters: user_id (the id of the user who contributed), project_name (the name of the project), and score (the bonus score).
-- The procedure first checks if the project exists. If it does not, it creates a new project with the given name.
-- Then, it retrieves the project's id using the project's name.
-- Finally, it inserts a new correction record into the corrections table with the user_id, project_id, and score parameters.


DELIMITER //
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT;
    IF (SELECT COUNT(*) FROM projects WHERE projects.name = project_name) = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END //
DELIMITER ;
