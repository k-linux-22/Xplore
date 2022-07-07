## Database Objects:

# Index:

 An Index is a database object. We create index to optimize the query performance and to get the sql results in lesser time.

If we create an index on a column, each value of the column along with row id will be stored as separate database object.

When we fire a query to fetch the data using this column in where clause, then the oracle engine will scan the index instead of entire table and will get the other column values using row id.

Row id is a Pseudo column used by Oracle to locate a row in database.

Types Of Index:

- **Normal indexes:** the default index type

- **Bitmap indexes:** store row ids associated with a key value as a bitmap

- **Partitioned indexes:** consist of partitions containing an entry for each value that appears in the indexed column(s) of the table.

- **Function-based indexes:** based on expressions. They enable to construct queries that evaluate the value returned by an expression, which in turn may include built-in or user-defined functions.

- **Domain indexes:** instances of an application-specific index of type indextype

---
**Index Creation:**

Syntax:
```
CREATE [UNIQUE] INDEX index_name ON table_name (column1, column2, ... column_n);
```
UNIQUE keyword is optional and it indicates that the combination of values in the indexed columns must       be unique.

Example:
```
CREATE INDEX products_idx ON products (product_name);
```
In this example, we have created an index on the products table called products_idx. It consists of only one field - the product_name field.

We could also create an index with more than one field as in the example below:
```
CREATE INDEX products_idx ON products (product_name, city);
```
Syntax To create  Bitmap index :
```
CREATE BITMAP INDEX ON TABLE_NAME(COLUMN_NAME);
```
If we need to create an index on a column having less number of distinct values, then we should create bitmap index.

Syntax To create function-based index :
```
CREATE INDEX product_idx ON products(UPPER(product_name));
```
---
**Advantages Of Indexes:**

- Indexes improve the query performance by avoiding the full table scans.

- Indexes are very useful with the tables having large amounts of data.

**Disadvantages Of Indexes:**

- Index is separate database object. For inserting new data or updating data in a table, the changes needs to be  reflected in the table as well as in the index object. Hence, the cost of DML operations increases.

- If we issue one insert statement on base table, oracle fires another insert statement internally to insert the data into index.

---
**Renaming Index:**

Syntax :
```
ALTER INDEX index_name RENAME TO new_index_name;
```
---
**Dropping Index:**

Syntax:
```
DROP INDEX index_name;
```
>Note: If the base table is dropped, all the indexes defined on the table will be dropped.