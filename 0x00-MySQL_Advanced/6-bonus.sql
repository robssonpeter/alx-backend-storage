-- Store Procedure for Adding bonus
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name TEXT, IN score FLOAT)
BEGIN
    -- check if the project exists
    SELECT id INTO @project FROM projects WHERE name = project_name;
    -- if not existing the create a new project
    IF @project IS NULL THEN
        INSERT INTO projects (`name`) VALUES (project_name);
        SELECT LAST_INSERT_ID() INTO @project;
    END IF;
    INSERT INTO corrections (`user_id`, `project_id`, `score`) VALUES (user_id, @project, score);
END //
DELIMITER ;
