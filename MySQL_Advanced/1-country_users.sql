-- Create a table named `users` with the following columns if it doesn't exist:
-- - `id` (integer, autoincrement, primary key)- `email` (string, not null, unique)
-- - `name` (string)
-- - `country` (enum, not null) with the following values: 'US', 'CO', 'TN' and the default value 'US'
CREATE TABLE IF NOT EXISTS `users` (
`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
`email` VARCHAR(255) NOT NULL UNIQUE,
`name` VARCHAR(255),
`country` ENUM('US','CO', 'TN') NOT NULL 
);
