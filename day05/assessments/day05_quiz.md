# Day 5 Quiz: Delta Lake Fundamentals

## Databricks Platform Administration Training
### Duration: 10 Minutes | 10 Questions | 70% to Pass

---

### Question 1
What are the two main components of a Delta Lake table?

- [ ] A) JSON files and CSV files
- [ ] B) Parquet data files and transaction log
- [ ] C) Avro files and metadata database
- [ ] D) ORC files and index files

---

### Question 2
Where is the Delta Lake transaction log stored?

- [ ] A) In a separate database
- [ ] B) In the _delta_log/ directory within the table
- [ ] C) In cloud provider's metadata service
- [ ] D) In the Databricks control plane

---

### Question 3
What does ACID stand for in database transactions?

- [ ] A) Advanced, Concurrent, Integrated, Durable
- [ ] B) Atomicity, Consistency, Isolation, Durability
- [ ] C) Automatic, Complete, Independent, Direct
- [ ] D) Asynchronous, Cached, Indexed, Distributed

---

### Question 4
How do you query a Delta table at a specific version?

- [ ] A) SELECT * FROM table WHERE version = 5
- [ ] B) SELECT * FROM table VERSION AS OF 5
- [ ] C) SELECT * FROM table@version5
- [ ] D) SELECT HISTORY FROM table VERSION 5

---

### Question 5
What is the default retention period for Delta Lake time travel?

- [ ] A) 1 day
- [ ] B) 7 days
- [ ] C) 30 days
- [ ] D) Forever

---

### Question 6
What does the VACUUM command do?

- [ ] A) Deletes all data from the table
- [ ] B) Removes data files no longer referenced by the transaction log
- [ ] C) Clears the query cache
- [ ] D) Compresses the transaction log

---

### Question 7
What does the OPTIMIZE command do?

- [ ] A) Deletes duplicate records
- [ ] B) Compacts small files into larger ones
- [ ] C) Updates table statistics
- [ ] D) Repairs corrupted files

---

### Question 8
Which SQL command shows the transaction history of a Delta table?

- [ ] A) SHOW HISTORY table_name
- [ ] B) DESCRIBE HISTORY table_name
- [ ] C) SELECT * FROM table_history
- [ ] D) VIEW TRANSACTIONS table_name

---

### Question 9
What happens when you RESTORE a Delta table to a previous version?

- [ ] A) The table is deleted and recreated
- [ ] B) A new version is created that matches the old version's state
- [ ] C) The transaction log is deleted
- [ ] D) All subsequent versions are permanently removed

---

### Question 10
What is Z-ORDER optimization used for?

- [ ] A) Sorting data alphabetically
- [ ] B) Co-locating related data to improve query performance
- [ ] C) Compressing files
- [ ] D) Creating indexes

---

## Answer Key

| Question | Answer | Explanation |
|----------|--------|-------------|
| 1 | B | Delta = Parquet files + Transaction log in _delta_log/ |
| 2 | B | Transaction log is in _delta_log/ directory within the table location |
| 3 | B | Atomicity, Consistency, Isolation, Durability |
| 4 | B | VERSION AS OF n syntax for querying specific versions |
| 5 | B | Default retention is 7 days (168 hours) |
| 6 | B | VACUUM removes unreferenced data files older than retention period |
| 7 | B | OPTIMIZE compacts small files into larger ones for better performance |
| 8 | B | DESCRIBE HISTORY shows all transactions on a Delta table |
| 9 | B | RESTORE creates a new version matching the historical state |
| 10 | B | Z-ORDER co-locates related data for faster queries on those columns |

---

*Quiz Version: 2.0 | Databricks Platform Administration Training - Day 5*
