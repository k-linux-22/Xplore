## Check Constraints

- CHECK constraint allows to apply conditions on a column(s),  to specifies the data/values to be allowed  in the column

- CHECK constraint validates the values in a given column to meet the specified criteria.
- CHECK constraint is used to limit the value range that can be placed in a column.

**Restrictions**

- The CHECK constraint can refer any column of the current table , but cannot refer any column of another table.

- CHECK constraint condition cannot include any view or sub query.

**Check constraint with Create statement (Column Level)**

A CHECK constraint can be defined on a table with the help of a CREATE statement.

Syntax :
```
CREATE TABLE table1 (col1 DATATYPE(size) CONSTRAINT cons_name
CHECK (condition), col2 DATATYPE(size) , ........);
```
Example:
```
CREATE TABLE person(name VARCHAR2(10), dob DATE, gender CHAR(1)
CONSTRAINT gndr_chk CHECK(gender IN ('M','F'));
```
The above example specified in the gender fields only the values 'M' or 'F' only need to be entered.

**Check constraint with Create statement (Table Level)**

A CHECK constraint can be defined as a table level definition once finishing all the column definitions.

Syntax :
```
CREATE TABLE table1 (col1 DATATYPE(size),col2 DATATYPE(size), ........,
CONSTRAINT cons_name CHECK (condition),CONSTRAINT cons_name CHECK (condition));
```

Example:
```
CREATE TABLE person(name VARCHAR2(10), gender CHAR(1),dob DATE,
CONSTRAINT gndr_chk CHECK(gender IN ('M','F'));
```
The above example specifies that gender fields only the values 'M' or 'F' only need to be entered.

**Check constraint with Alter statement**

Suppose a table has been created without a CHECK constraint and later it was  identified to maintain a CHECK constraint in the table , this can be achieved with the  help of ALTER statement.

Syntax:
```
ALTER TABLE table2 ADD CONSRAINT cons_name CHECK (condition);
```
Example: 
```
CREATE TABLE person(name VARCHAR2(10), gender CHAR(1),dob DATE);
ALTER TABLE person ADD CONSTRAINT gndr_chk CHECK(gender IN ('M','F'));
```
The above example specifies that gender fields only the values 'M' or 'F' only need to be entered.

In order to remove a CHECK constraint which is defined on a table , we need to drop the constraint defined.

Syntax:
```
ALTER TABLE table1 DROP CONSTRAINT cons_name;
```
Example:
```
ALTER TABLE person DROP CONSTRAIN gndr_chk;
```
From the above example we can observe that if at all the government does not want to maintain a CHECK constraint for the gender field, that can be removed.