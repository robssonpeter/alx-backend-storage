-- the script to create a new view need meeting
CREATE VIEW need_meeting AS
SELECT * FROM students
WHERE score < 80 AND (last_meeting IS NULL OR DATEDIFF(DATE(NOW()), last_meeting));