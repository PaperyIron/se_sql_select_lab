# STEP 1A
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# STEP 2
# Replace None with your code
df_first_five = pd.read_sql_query("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)

# print(df_first_five)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql_query("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)

# print(df_five_reverse)
# STEP 4
# Replace None with your code
df_alias = pd.read_sql_query("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""", conn)

# print(df_alias)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql_query("""
    SELECT *,
        CASE 
            WHEN jobTitle = "President" OR jobTitle = "VP Sales" OR jobTitle = "VP Marketing" THEN "Executive"
            ELSE "Not Executive"
        END AS role
    FROM employees                    
""", conn)

# print(df_executive)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql_query("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)

# print(df_name_length)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql_query("""
    SELECT substr(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)

# print(df_short_title)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql_query("""
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_prices
    FROM orderDetails
""", conn).iloc[0]

# print(sum_total_price)

# STEP 9
# Replace None with your code


df_day_month_year = pd.read_sql_query("""
    SELECT orderDate,
           STRFTIME('%d', orderDate) AS day,
           STRFTIME('%m', orderDate) AS month,
           STRFTIME('%Y', orderDate) AS year
    FROM orders
""", conn)

# print(df_day_month_year)

# Add the code below and run the file to see order details data


conn.close()