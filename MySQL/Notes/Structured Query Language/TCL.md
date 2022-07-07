## Introduction to Transaction Control

Oracle server ensures data consistency based upon transactions. Transactions consist of DML statements that make up one consistent change tothe data.

---

**Transaction Start and End Scenarios:**

A Transaction begins when the first executable sql statement is encountered. The Transaction terminates when the following specifications occur.

- A COMMIT or ROLL BACK issued.
- A DDL statement issued
- A DCL statement issued
- Failure of machine or system crashes
- A DDL or DCL statement is automatically committed and hence implicitly ends a Transaction.

---

**Explicit Transaction Control Statements**

- COMMIT
- SAVEPOINT
- ROLLBACK
- COMMIT

It ends the current Transaction by making all pending data changes permanent.

Syntax: 
```
COMMIT;
```
Once commit is issued, data changes will become permanent.
The previous state of the data is permanently lost.
All users can view the results of the recent transactional changes.

Example: 
```
UPDATE employee SET salary =1000 WHERE emp_id = 10;
COMMIT;
```

---

**SAVEPOINT:**

It marks a savepoint with in the current Transaction. We can create multiple savepoints in single Transaction.Savepoints can be used to control the reverting of changes.

Syntax:
```
SAVEPOINT ;
```
Ex: 
```
SAVEPOINT S1;
```

---
**ROLLBACK:**

- It ends the current Transaction by discarding all pending data changes.
- The data changes are undone.
- The previous state of data is restored.
- The locks on the affected rows are automatically released.

Syntax: 
```
ROLLBACK or ROLLBACK to ;
```
Ex: 
```
UPDATE employee SET salary =1000 WHERE emp_id = 10;
ROLLBACK;
```
Using savepoint, the Transaction can be discarded up to the marker by using rollback statement.

Ex:
```
INSERT INTO employee VALUES(10,'JHON',3000);
INSERT INTO employee VALUES(10,'KELLY',2000);
SAVEPOINT S1;
INSERT INTO employee VALUES(10,'WILSON',4000);
ROLLBACK TO S1;
```
