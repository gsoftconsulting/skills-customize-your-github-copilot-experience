# 📘 Assignment: SQL Foundations with Microsoft SQL Server

## 🎯 Objective

Practice writing beginner-friendly SQL queries using Microsoft SQL Server. You will retrieve, filter, sort, and summarize school data from related tables.

## 📝 Tasks

### 🛠️	Set Up and Explore the Tables

#### Description
Run the provided starter SQL script to create and populate two tables: `Students` and `Grades`. Then write simple queries to inspect the data.

#### Requirements
Completed program should:

- Execute the starter SQL script without errors.
- Display all rows from `Students` and all rows from `Grades`.
- Show only `student_name` and `grade_level` from `Students`.


### 🛠️	Write Core SQL Queries

#### Description
Create SQL queries that answer classroom questions using filtering, sorting, joins, and aggregation.

#### Requirements
Completed program should:

- Return students in grade 10 sorted by `student_name` (A to Z).
- Use an `INNER JOIN` between `Students` and `Grades` to show each student's `student_name`, `subject`, and `score`.
- Return all math scores greater than or equal to 85.
- Show the average score for each subject using `GROUP BY`.
