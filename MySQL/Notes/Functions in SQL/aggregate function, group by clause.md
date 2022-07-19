## Aggregate / Group Functions:

Group Functions, as the name suggests, are functions that operate on groups(sets) of values and returns one result per group.

Group function returns a single result row for every group of queried rows.

Based on the query statement it may return single or multiple rows.

The functions that are used as Aggregate Functions are:
- SUM
- AVG
- MAX
- MIN
- COUNT

Consider the following table: 

Employee

---
**AVG:** 

Returns an average value, ignoring null values.

Syntax:
```
AVG([DISTINCT] column_name)
```
Ex: 
```
SELECT AVG(salary) as “Average Salary” FROM Employee;
---
Output :
Average Salary
21500
```
The above query displays the average salary of all the employees in the table
Employee

---
**MAX:**

Returns the maximum value, ignoring null values.

Syntax: 
```
MAX([DISTINCT] column_name)
```
Ex: 
```
SELECT MAX(salary) as “Maximum Salary” FROM Employee where
Dep_Name='HR';
---
Output :
Maximum Salary
16000
```
The above query displays the maximum salary of all the employees in HR Department in the table Employee.

---
**MIN:** 

Returns the minimum value, ignoring null values.

Syntax:
```
MIN([DISTINCT] column_name)
```
Ex: 
```
SELECT MIN(salary) as “Minimum Salary” FROM Employee where
Dep_Name='HR';
---
Output :
Minimum Salary
10000
```
The above query displays the minimum salary of all the employees in HR Department in the table Employee.

---
**COUNT:** 

Returns the count of not null values ignoring null values.

Syntax:
```
COUNT([DISTINCT] column_name)
```
Ex: 
```
SELECT COUNT(DISTINCT Dep_name) Departments FROM Employee;
---
3
```
The above query displays the count of different departments in the table Employee.

---
**COUNT:(*)** 

Count function with asterisk returns the count of total number of rows including null values.

Syntax:
```
COUNT(*)
```
Ex: 
```
SELECT COUNT(*) FROM Employee;
---
5
```
The above query displays the total number of rows in table Employee.

---
## GROUP BY clause

Creates a data set, containing several sets of records grouped together based on a condition.

Syntax:
```
SELECT [,], AGGREGATE FUNCTION() FROM Table_Name GROUP BY [,] ;
```
Ex: 
```
SELECT dep_name,COUNT(emp_id) "No of Employee" FROM Employee GROUP BY dep_name;
---
Output : 
    No of Employee
HR 2
Marketing 2
Admin 1
```
The above query displays the number of employee in each department.

---
## WHERE clause

Used to apply a filter condition before the Grouping the rows.

Syntax:
```
SELECT [,], AGGREGATE FUNCTION() FROM Table_Name WHERE GROUP BY [,] ;
```
Ex: 
```
SELECT Dep_Name,COUNT(Salary) FROM Employee WHERE
Salary>15000 GROUP BY Dep_Name;
---
Output : 

HR 1
Marketing 1
Admin 1
```
The above query displays department wise count of salary more than 15000.

---
## HAVING clause

Used to apply a filter condition on Aggregated values.

Syntax:
```
SELECT [,], AGGREGATE FUNCTION() FROM Table_Name WHERE GROUP BY [,] HAVING ;
```
Ex: 
```
SELECT Dep_Name, SUM(Salary) FROM Employee WHERE Salary>12000
GROUP BY Dep_Name HAVING SUM(Salary)<30000;
---
Output :
HR 16000
Marketing 20000
```
The above query displays the departments for which total salary is less 30000
excluding the Admin department, total salary for which is 40000.

