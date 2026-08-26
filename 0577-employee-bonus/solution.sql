# Write your MySQL query statement below
SELECT a.name, b.bonus
FROM Employee a
LEFT JOIN Bonus b
ON a.empId=b.empId
WHERE 1=1 AND
b.bonus < 1000 OR
bonus IS NULL;


