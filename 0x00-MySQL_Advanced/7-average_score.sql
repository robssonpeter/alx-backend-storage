-- Script for Average Score Computation Procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    SELECT AVG(score) INTO @average FROM corrections WHERE user_id = @user_id;
    UPDATE users SET average_score = @average WHERE id = user_id;
END //
DELIMITER ;