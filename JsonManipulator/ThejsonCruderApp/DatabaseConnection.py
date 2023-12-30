import mysql.connector as mc

class DataBase:
    
    def __init__(self):
        
        self.user = 'root'
        self.password = 'mysql'
        self.host = '127.0.0.1'
        self.port = '3306'
        self.databaseName = 'basic_api_service'
        
    def connectDataBase(self):
        
        # Establish a connection to the database using the required parameters
        dbObject = mc.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.databaseName
        )
        return dbObject

    def queryExecution(self, query, data):
        # Create a database cursor and execute the specified query
        # Connect to the database
        
        DataBaseObject = self.connectDataBase()
        DataBaseCusor = DataBaseObject.cursor()
        
        try:
            
            # If the query is a SELECT statement, execute it and return the result
            if('SELECT' in query):
                # Execute the query with the specified data
                DataBaseCusor.execute(query,data)
                # Retrieve all the rows returned by the query
                result = DataBaseCusor.fetchall()
                # Return the result
                return result
            
            # If the query is an UPDATE or INSERT statement, execute it and commit the changes
            elif('UPDATE' or 'INSERT' in query):
                # Execute the query with the specified data
                DataBaseCusor.execute(query,data)
                # Commit the changes to the database
                DataBaseObject.commit()
                # Return True to indicate that the query was successful
                return True
            
        except mc.Error as error:
            
            # If there is an error executing the query, print an error message
            print("parameterized query failed {}".format(error)) 
            
        finally:
            
            # Close the database cursor and connection
            if DataBaseObject.is_connected():
                DataBaseObject.close()
                DataBaseCusor.close()
         
               
        
        
                
                
                