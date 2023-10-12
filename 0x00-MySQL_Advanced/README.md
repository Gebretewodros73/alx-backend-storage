# 0x00-MySQL_Advanced

## Description

This directory contains a collection of MySQL projects focusing on advanced concepts within the scope of the ALX Backend Storage curriculum. Each sub-directory corresponds to a specific project, and within each sub-directory, you'll find SQL scripts and instructions related to that project.

## Projects

1. [0-uniq_users.sql](./0-uniq_users.sql): Creates a table `users` with specified attributes and ensures email uniqueness.
2. [1-country_users.sql](./1-country_users.sql): Creates a table `users` with an additional attribute `country` and specified constraints.
3. [2-fans.sql](./2-fans.sql): Ranks country origins of bands based on the number of fans.
4. [3-glam_rock.sql](./3-glam_rock.sql): Lists bands with Glam rock as their main style, ranked by longevity.
5. [4-store.sql](./4-store.sql): Creates a trigger that decreases the quantity of an item after adding a new order.
6. [5-valid_email.sql](./5-valid_email.sql): Creates a trigger that resets the attribute valid_email only when the email has been changed.
7. [6-bonus.sql](./6-bonus.sql): Creates a stored procedure `AddBonus` that adds a new correction for a student.
8. [7-average_score.sql](./7-average_score.sql): Creates a stored procedure `ComputeAverageScoreForUser` that computes and stores the average score for a student.
9. [8-index_my_names.sql](./8-index_my_names.sql): Creates an index on the first letter of names.
10. [9-index_name_score.sql](./9-index_name_score.sql): Creates an index on the first letter of names and the score.
11. [10-div.sql](./10-div.sql): Creates a function `SafeDiv` that safely divides two numbers.
12. [11-need_meeting.sql](./11-need_meeting.sql): Creates a view `need_meeting` listing students requiring a meeting based on their scores and last meeting dates.
13. [100-average_weighted_score.sql](./100-average_weighted_score.sql): Creates a stored procedure `ComputeAverageWeightedScoreForUser` for computing and storing the average weighted score for a student.
14. [101-average_weighted_score.sql](./101-average_weighted_score.sql)Write a SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUsers` that computes and stores the average weighted score for all students.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/gebretewodros73/alx-backend-storage.git
   ```
2. Navigate to the desired project directory:

   ```bash
   cd alx-backend-storage/0x00-MySQL_Advanced
   ```
