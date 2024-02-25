import mysql.connector

def initialize_connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "abcd123",
        database = "mlis"
    )
    conn.autocommit = True

    cursor = conn.cursor()
    cursor.execute("show tables;")
    temp = cursor.fetchall()
    tables = [item[0] for item in temp]
    print(tables)
    cursor.execute("DESC user;")
    print(cursor.fetchall())
    return conn, cursor

conn, cursor = initialize_connection()

def login(cursor, d):
    cursor.execute(f"""SELECT UserType FROM user WHERE UserName='{d[0]}' AND Password='{d[1]}'""")
    # rows = cursor.fetchall()
    # for row in rows:
    #     current_username, current_password = row
    #     if current_username == d[0] and current_password == d[1]:
    #         return True
    # return False
    return cursor

def register(cursor, data):
    cursor.execute("""SELECT UserID FROM user ORDER BY UserID DESC LIMIT 1""")
    userid = [item[0] for item in cursor]
    userid = int(userid[0]) + 1
    cursor.execute(f"""INSERT INTO user VALUES (
                   '{userid}',
                   '{data["Name"]}',
                   '{data["Email"]}',
                   '{data["Password"]}',
                   '{data["UserType"]}',
                   {data["Age"]},
                   '{data["Gender"]}'
                   )""")




# Admin
cursor.execute("SELECT LabName, LabID FROM lab;")
labnames = [item[0] for item in cursor]
print(labnames)

cursor.execute("SELECT TestName, TestID FROM test;")
testnames = [item[0] for item in cursor]
print(testnames)


def lab_add(data):
    cursor.execute("""SELECT LabID FROM lab ORDER BY LabID DESC LIMIT 1""")
    labid = [item[0] for item in cursor]
    labid = int(labid[0]) + 1
    cursor.execute(f"""INSERT INTO lab VALUES (
                   '{labid}',
                   '{data["LabName"]}',
                   '{data["ContactNo"]}',
                   '{data["Location"]}',
                   {data["OpenHrs"]},
                   {data["YrsOfExp"]}
    )""")
    return cursor

def test_add(data):
    cursor.execute("""SELECT TestID FROM test ORDER BY TestID DESC LIMIT 1""")
    testid = [item[0] for item in cursor]
    testid = int(testid[0]) + 1
    cursor.execute(f"""INSERT INTO test VALUES (
                   '{testid}',
                   '{data["TestName"]}',
                   '{data["Description"]}',
                   '{data["SampleType"]}',
                   '{data["TestDuration"]}',
                   '{data["NormalRange"]}'
    )""")
    return cursor

def efficiency_add(data):
    cursor.execute(f"""SELECT LabID FROM lab WHERE LabName='{data["Lab"]}'""")
    for item in cursor:
        labid = item[0]
    cursor.execute(f"""SELECT TestID FROM test WHERE TestName='{data["Test"]}'""")
    for item in cursor:
        testid = item[0]
    cursor.execute(f"""INSERT INTO efficiency VALUES (
                   '{labid}',
                   '{testid}',
                   {data["Price"]},
                   {data["TestsPerDay"]},
                   '{data["Sensitivity"]}',
                   '{data["Specificity"]}'
    )""")
    return cursor


def lab_update(data):
    pass

def test_update(data):
    pass

def efficiency_update(data):
    pass


def lab_delete(data):
    cursor.execute(f"""DELETE FROM lab WHERE LabName='{data["LabName"]}'""")
    return cursor

def test_delete(data):
    cursor.execute(f"""DELETE FROM test WHERE TestName='{data["TestName"]}'""")
    return cursor

def efficiency_delete(data):
    cursor.execute(f"""SELECT LabID FROM lab WHERE LabName='{data["Lab"]}'""")
    for item in cursor:
        labid = item[0]
    cursor.execute(f"""SELECT TestID FROM test WHERE TestName='{data["Test"]}'""")
    for item in cursor:
        testid = item[0]
    cursor.execute(f"""DELETE FROM efficiency WHERE LabID='{labid}' AND TestID='{testid}'""")



# Patient
def search(t):
    cursor.execute(f"""SELECT t.TestName, l.LabName, l.ContactNo, l.Location, 
                   e.Price, l.OpenHrs, l.YrsOfExp, t.Description, t.SampleType, 
                   t.TestDuration, e.TestsPerday, e.Sensitivity, e.Specificity 
                   FROM lab l, test t, efficiency e WHERE t.TestID=e.TestID AND 
                   t.TestID=e.TestID AND t.TestName='{t}'
                   """)
    print(cursor.fetchall())