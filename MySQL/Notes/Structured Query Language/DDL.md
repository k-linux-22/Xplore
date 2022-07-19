## Data Definition Language (DDL) 
DDL statements define the data structure such as tables, views etc.. that make up the database. All DDL statements are auto committed means the changes will become permanent and database objects created are available to all users.
Commonly used DDL statements are:

* CREATE
* ALTER
* DROP
* RENAME
* TRUNCATE

**Data types**

A data type identifies or classifies a particular type of information or data. Some commonly used data types are:

- CHAR (size) - Used to store character strings values of fixed length.
- VARCHAR2 (size) – Used to store variable length string data.
- NUMBER (size, precision) – Used to store numbers(fixed or floating point)
- DATE – Used to represent date and time.
- LONG – Used to store large variable length strings(upto 2GB).

---

**DDL statement : CREATE**

The CREATE keyword is used for creating database objects like tables, views,triggers, and indexes

**Syntax:**

```
CREATE TABLE table_name
(
column_name1 DATATYPE(Size) ,
column_name2 DATATYPE(Size),
column_name3 DATATYPE(Size)
);
```

Example: 
``` 
Create Table Employee
(
Emp_id number(4) NOT NULL,
Name varchar2(20) NOT NULL,
Salary number(8),
E_Mail varchar2(30),
Country varchar2(20),
);
```

The above statement creates a table named Employee with columns Emp_id, name, Salary, E_Mail and Country.

---

**DDL statement : ALTER**

Alter statement is used to modify the structure of database or database objects like tables, views etc..


Alter table statement - to add column to a table:

![Alter Table](https://g91.tcsion.com/per/g91/pub/2030/LX/ckeditor_assets/pictures/2030/152/sq1_original.jpg "Alter Table")

The above statement adds a new column 'age' of number data type with
constraint not null.


**Modifying the column**

**Ex:** 
```
ALTER TABLE Employee MODIFY salary number(10,2);
```
Table Altered.

**Rename and Drop a Column**

Using the alter statement we can rename a column and also the drop any column.

![Alter Table](https://g91.tcsion.com/per/g91/pub/2030/LX/ckeditor_assets/pictures/2030/512/alter_original.jpg "Alter Table")

The above statements renames the column name salary to em_sal anddrops column age

---

**DDL statements : TRUNCATE , DROP , RENAME**

**Truncate Table:**

Remove all the rows and resets schema of the table.
```
TRUNCATE TABLE Employee;
```

**Drop Table:**

Deletes table entirely from the database.
```
DROP TABLE Employee;
```

**Renaming a Table:**

Changing the name of a table.
```
RENAME Employee to Emp_table;
```
