import pyodbc
print(pyodbc.drivers())

print("--------------------------")


conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"  # Note the double backslash
    "Database=Godrej_Boys;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)
print("--------------------------")

cursor = conn.cursor()


print("--------------------------")
print(cursor)

print("--------------------------")
