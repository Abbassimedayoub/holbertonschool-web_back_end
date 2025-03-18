# Redis - In-Memory Data Store

Redis is an open-source, in-memory key-value store. It is often used as a database, cache, and message broker. Redis supports a variety of data structures, such as strings, hashes, lists, sets, and more.

## Table of Contents

- [Redis - In-Memory Data Store](#redis---in-memory-data-store)
  - [Table of Contents](#table-of-contents)
  - [What is Redis?](#what-is-redis)
  - [Installation](#installation)
    - [On Ubuntu](#on-ubuntu)

## What is Redis?

Redis is a fast, open-source, in-memory key-value data store. It supports a wide range of data types and provides features like persistence, replication, and high availability.

Redis can be used for various purposes, including caching, session storage, real-time analytics, message queues, and more.

## Installation

### On Ubuntu

1. Update the package list and install Redis:

   ```bash
   sudo apt-get update
   sudo apt-get install redis-server
   ```

2. Enable and start Redis:
    ```bash
    sudo systemctl enable redis-server
    sudo systemctl start redis-server
    ```

