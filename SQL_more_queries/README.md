# SQL More Queries

This project focuses on advanced SQL concepts using MySQL.
You will practice creating users, managing privileges, defining tables with constraints, and writing complex queries involving joins, subqueries, grouping, and aggregations.

The project builds on basic SQL knowledge and emphasizes data relationships and query optimization.

## Technologies
* MySQL 8.0
* Ubuntu 20.04 LTS
* SQL scripts executed using the MySQL CLI

## Project Structure
```pgsql
SQL_more_queries/
├── 0-privileges.sql
├── 1-create_user.sql
├── 2-create_read_user.sql
├── 3-force_name.sql
├── 6-states.sql
├── 7-cities.sql
├── 8-cities_of_california.sql
├── 9-cities_by_state.sql
├── 10-genre_id_by_show.sql
├── 11-genre_id_all_shows.sql
├── 12-no_genre.sql
├── 13-count_shows_by_genre.sql
├── 14-my_genres.sql
├── 15-comedy_only.sql
├── 16-shows_by_genre.sql
├── 100-not_my_genres.sql
├── 101-not_a_comedy.sql
├── 102-rating_shows.sql
├── 103-rating_genres.sql
└── README.md
```

## Learning Objectives

By completing this project, you will learn how to:
* Create and manage MySQL users and privileges
* Use PRIMARY KEY, FOREIGN KEY, and NOT NULL constraints
* Write JOIN, LEFT JOIN, and subqueries
* Perform aggregations using COUNT, SUM, and GROUP BY
* Filter and sort query results
* Handle missing relationships using NULL
* Write SQL scripts that are idempotent (safe to run multiple times

## How to Run Scripts
```bash
cat script_name.sql | mysql -hlocalhost -uroot -p database_name
```

* Example:
```bash
cat 9-cities_by_state.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
```

## Database Dumps

**Some tasks require importing database dumps:**
* ```hbtn_0d_tvshows.sql```
* ```hbtn_0d_tvshows_rate.sql```

**Import them using:**
```bash
mysql -uroot -p < dump_file.sql
```

## Requirements

* All SQL files must end with a new line
* Only one SELECT allowed where specified
* No hardcoded database names unless required
* Scripts must not fail if objects already exist
* MySQL keywords should be written in uppercase

## Author
* **Yara Alrasheed**
* Holberton School Student
