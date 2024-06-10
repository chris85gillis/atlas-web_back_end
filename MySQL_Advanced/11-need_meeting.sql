-- This view will display the names of students who need to meet
-- with the advisor. A student needs a meeting if their score is
-- below a certain threshold (80 in this case) and either they
-- haven't had a meeting in the past month or they haven't
-- had a meeting at all.


CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
    AND (
        last_meeting IS NULL
        OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
