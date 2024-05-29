import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db')

table_name = 'INSTRUCTOR'
table_name2 = 'Departments'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']
attribute_list2 = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID',]
file_path = 'INSTRUCTOR.csv'
file_path2 = 'Departments.csv'
df = pd.read_csv(file_path, names = attribute_list)
df2 = pd.read_csv(file_path2, names = attribute_list2)
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
df2.to_sql(table_name2, conn, if_exists = 'replace', index =False)
print('Table is ready')


# Viewing all the data in the table.
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing only FNAME column of data.
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


# Viewing the total number of entries in the table.
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


# Appending Data to existing Table:
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')
# conn.close()
# Appending Data to existing Table(Departments):
data_dict2 = {'DEPT_ID' : [9],
            'DEP_NAME' : ['Quality Assurance'],
            'MANAGER_ID' : [30010],
            'LOC_ID' : ['L0010'],
            }
data_append2 = pd.DataFrame(data_dict)

data_append2.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data2 appended successfully')
conn.close()


# failure to get data from wget
#  wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/INSTRUCTOR.csv