## Data Manipulation Language

Data Manipulation Language(DML) is a structured query language which is used for inserting, updating and deleting data in the database objects like table or view.

DML comprises the SQL change statements which modifies the stored data but not the database object.

DML consist of three SQL statements namely:
- Insert
- Update
- Delete

---

**INSERT Statement**

 Insert statement is used for inserting data into table.
 Insertion of data can be done in multiple ways.

**Syntax:**
```
INSERT INTO table_name[(column1, column2,...)]
VALUES(value1, value2,....);
```
![insert](https://g91.tcsion.com/per/g91/pub/2030/LX/ckeditor_assets/pictures/2030/154/sq3_original.jpg "insert")

If values in all the columns inserted in proper order, column names are not mandatory.

**Syntax:**
```
INSERT INTO table_name VALUES(value1, value2,....);
```
![insert](https://g91.tcsion.com/per/g91/pub/2030/LX/ckeditor_assets/pictures/2030/155/sq4_original.jpg "insert")

**Insert Multiple Rows:**

We  can insert multiple rows using a **single** INSERT statement:

Syntax:
```
INSERT INTO table_name (col1,col2,..) VALUES 

    (.....values for record 1),

    (.....values for record 1),

    ........

    (values for record n); 
```
Example:    
```
INSERT INTO cities (city_name, state) VALUES
    ('Guwahati', 'Assam'),
    ('Shillong', 'Meghalaya'),
    ('Imphal', 'Manipur');
```
> Note: In the video available in this course , the syntax used to insert multiple rows to a table is supported by Oracle not by MySQL. 

---

**UPDATE statement**

Update command is used to change or modify data of one or more records in a table.

**Syntax:**
```
UPDATE Table_name SET Column_name1=value1
[,Column_name2=value2,...]
[WHERE Condition];
```
All rows will be updated if no condition is specified in where clause.

![update](https://g91.tcsion.com/per/g91/pub/2030/LX/ckeditor_assets/pictures/2030/157/sq6_original.jpg "update")

---

**DELETE statement**

Delete statement is used to remove one or more records from a table.
A subset may be defined for deletion using a condition, otherwise all records are removed.

**Syntax:**
```
DELETE FROM Table_Name [WHERE Condition];
```
Delete statement using WHERE condition.

![delete using where](https://g91.tcsion.com/per/g91/pub/2030/LX/ckeditor_assets/pictures/2030/158/sq7_original.jpg "delete using where")

> Note: Delete statement without where condition deletes all the rows from table.

Example:

![delete without using where](https://g91.tcsion.com/per/g91/pub/2030/LX/ckeditor_assets/pictures/2030/158/sq7_original.jpg "delete without using where")