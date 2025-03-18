# MySQL Project README

## Overview
This repository contains SQL scripts and configurations for managing a MySQL database. It includes essential queries for database creation, table structure, relationships, and common operations such as inserting, updating, deleting, and querying data.

## Table of Contents
- [MySQL Project README](#mysql-project-readme)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
    - [1. Installation](#1-installation)
    - [2. Database Setup](#2-database-setup)
    - [3. Usage](#3-usage)
    - [4. Schema](#4-schema)
      - [Tables:](#tables)
      - [Example Table Creation Query:](#example-table-creation-query)
    - [5. Backup and Restore](#5-backup-and-restore)
    - [6. Troubleshooting](#6-troubleshooting)

---

### 1. Installation

Follow these steps to install MySQL on your local machine or server:

- **For Linux (Ubuntu/Debian):**
    ```bash
    sudo apt update
    sudo apt install mysql-server
    sudo mysql_secure_installation
    ```

- **For macOS:**
    Install MySQL using Homebrew:
    ```bash
    brew install mysql
    brew services start mysql
    ```

- **For Windows:**
    Download and install MySQL from the [official MySQL website](https://dev.mysql.com/downloads/installer/). 

After installation, you can access MySQL using:
```bash
mysql -u root -p
```
### 2. Database Setup

After MySQL is installed, follow these steps to set up the database:

1. **Login to MySQL**:
    ```bash
    mysql -u root -p
    ```

2. **Create the database**:
    ```sql
    CREATE DATABASE my_database;
    ```

3. **Select the database**:
    ```sql
    USE my_database;
    ```

4. Run the provided SQL scripts to create tables, relationships, and insert sample data.

---

### 3. Usage

Once the database is set up, you can start using the MySQL queries included in this project. Some common queries include:

- **Inserting Data**:
    ```sql
    INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
    ```

- **Selecting Data**:
    ```sql
    SELECT * FROM users;
    ```

- **Updating Data**:
    ```sql
    UPDATE users SET email = 'john.doe@example.com' WHERE name = 'John Doe';
    ```

- **Deleting Data**:
    ```sql
    DELETE FROM users WHERE name = 'John Doe';
    ```

---

### 4. Schema

This project uses the following schema:

#### Tables:
1. **users**  
   - `id` (INT, Primary Key, Auto Increment)
   - `name` (VARCHAR(255))
   - `email` (VARCHAR(255))

2. **orders**  
   - `id` (INT, Primary Key, Auto Increment)
   - `user_id` (INT, Foreign Key referencing `users.id`)
   - `product_name` (VARCHAR(255))
   - `order_date` (DATETIME)

#### Example Table Creation Query:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
```
---

### 5. Backup and Restore

- **Backup a MySQL Database**:
    ```bash
    mysqldump -u root -p my_database > my_database_backup.sql
    ```

- **Restore a MySQL Database**:
    ```bash
    mysql -u root -p my_database < my_database_backup.sql
    ```

---

### 6. Troubleshooting

Here are some common issues you might encounter and their solutions:

- **Issue: Access Denied for User**  
  **Solution:** Make sure you're logging in with the correct user and password. If the user doesn’t have sufficient privileges, grant them using:
  ```sql
  GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
 ``` 

