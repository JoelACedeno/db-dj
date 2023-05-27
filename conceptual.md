### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  - PostgreSQL is a command line tool that allows you to interact with SQL databases

- What is the difference between SQL and PostgreSQL?
  - SQL is the language, PSQL is the tool used to interact with the SQL db using SQL language

- In `psql`, how do you connect to a database?
  - \c database_name

- What is the difference between `HAVING` and `WHERE`?
  - `WHERE` is used to select from the source based on a condition, `HAVING` is used as a condition together with the `GROUP BY` clause

- What is the difference between an `INNER` and `OUTER` join?
  - Inner join selects all things that are in common between tables, outer join selects things that are in common and are different between tables

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  - `LEFT OUTER` selects all rows from the left table and the matching rows from the right table. `RIGHT OUTER` selects all rows from the right table and the matching rows from the left table.

- What is an ORM? What do they do?
  - Object Relational Mapping: provides a way to map database tables and their relatonships to classes and objects in code

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
    - When you use AJAX some sensitive data can be easily accessed through the client, when you use a library the data is more secure from attacks.

- What is CSRF? What is the purpose of the CSRF token?
  - A CSRF token is a security measure designed to protect against Cross Site Request Forgery. Without it malicious sites can make requests to other sites where the user is authenticated.

- What is the purpose of `form.hidden_tag()`?
  - `hidden_tag()` allows the form to be generated with a CSRF token validating that the submisson came from the application and not a malicious source
