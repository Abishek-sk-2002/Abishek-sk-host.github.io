from .DatabaseConnection import DataBase

def listUserData():
    query = (''' SELECT * FROM user_details ''')
    data = ()
    db_object = DataBase()
    result = db_object.queryExecution(query,data)
    return result

def insertUserDetails(user_name, email_id):
    query = f'''INSERT INTO user_details(username, email) VALUES (%s, %s)'''
    data = (user_name, email_id,)
    print("Executing query:", query)
    print("Data:", data)
    db_object = DataBase()
    result = db_object.queryExecution(query, data)
    return result

def updateUserDetails(user_id,user_name,email_id):
    query = f'''UPDATE user_details SET username = %s, email = %s WHERE user_id = '{user_id}' '''
    data = (user_name,email_id)
    print(query)
    print(data)
    db_object = DataBase()
    result = db_object.queryExecution(query,data)
    return result

