# SQL – Introduction

This project is part of the Higher Level Programming curriculum at Holberton School and introduces MySQL fundamentals.

The goal is to learn how to manage databases and tables, manipulate data, and perform queries using SQL while following strict formatting and style requirements.

## Learning Objectives
By completing this project, you should be able to:
* Create and delete MySQL databases
* Create, modify, and describe tables
* Insert, update, delete, and query records
* Use SQL aggregate functions
* Filter, group, and sort query results
* Work with character sets and collations
* Execute SQL scripts from the command line

## File Description

| File                               | Description                                   |
| ---------------------------------- | --------------------------------------------- |
| `0-list_databases.sql`             | Lists all databases                           |
| `1-create_database_if_missing.sql` | Creates a database if it does not exist       |
| `2-remove_database.sql`            | Deletes a database if it exists               |
| `3-list_tables.sql`                | Lists all tables of the current database      |
| `4-first_table.sql`                | Creates a table called `first_table`          |
| `5-full_table.sql`                 | Prints the full description of `first_table`  |
| `6-list_values.sql`                | Lists all rows of `first_table`               |
| `7-insert_value.sql`               | Inserts a new row into `first_table`          |
| `8-count_89.sql`                   | Counts records with a specific value          |
| `9-full_creation.sql`              | Creates and populates `second_table`          |
| `10-top_score.sql`                 | Lists records ordered by best score           |
| `11-best_score.sql`                | Lists records with score ≥ 10                 |
| `12-no_cheating.sql`               | Updates Bob’s score                           |
| `13-change_class.sql`              | Deletes records with low scores               |
| `14-average.sql`                   | Computes the average score                    |
| `15-groups.sql`                    | Counts records grouped by score               |
| `16-no_link.sql`                   | Lists records with a valid name               |
| `100-move_to_utf8.sql`             | Converts database and table to UTF8           |
| `101-avg_temperatures.sql`         | Displays average temperature by city          |
| `102-top_city.sql`                 | Displays top 3 hottest cities (July & August) |
| `103-max_state.sql`                | Displays max temperature per state            |
| `README.md`                        | Project documentation                         |

## Requirements
* MySQL 8.0
* Ubuntu 22.04 LTS
* All SQL keywords in uppercase
* Each file:
  * Starts with a comment describing the task
  * Has a comment before each SQL query
  * Ends with a newline
* A README.md file is mandatory

## Usage
Run SQL scripts using:
```bash
cat filename.sql | mysql -hlocalhost -uroot -p database_name
```
Example:
```bash
cat 3-list_tables.sql | mysql -uroot hbtn_0c_0
```

## Concepts Covered
* Database management
* Table creation and modification
* CRUD operations
* Aggregate functions (COUNT, AVG, MAX)
* Filtering and sorting (WHERE, ORDER BY)
* Grouping (GROUP BY)
* Character sets and collations
* SQL scripting

## Author
**Yara K. Alrasheed**
📧 Email: 11982@holbertonschool.com
🐙 GitHub: 11982-yr
