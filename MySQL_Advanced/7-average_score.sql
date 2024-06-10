-- This stored procedure computes the average score for a given user and updates the average_score field in the users table.


DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id int) 
BEGIN
    DECLARE total_score INT;
    DECLARE nb_scores INT;
    DECLARE average_score DECIMAL(5,2);

    SELECT SUM(score) INTO total_score, COUNT(score) INTO nb_scores FROM corrections WHERE user_id = user_id;

    SET average_score = total_score / nb_scores;

    UPDATE users SET average_score = average_score WHERE id = user_id;
END //
DELIMITER ;
