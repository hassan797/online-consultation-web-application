# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 22:32:31 2021

@author: WarPeace101
"""
#final
import sqlite3
import pyodbc
from beautifultable import BeautifulTable

def printTable(cursor, tableName):
    SQL = 'SELECT * from '+tableName+''
    cursor.execute(SQL)
    columns = cursor.description
    result = cursor.fetchall()
    table = BeautifulTable()
    for i in result:
        table.rows.append(i)
    temp = []
    for i in columns:
        temp.append(i[0])
    
    table.columns.header = temp
    print(table)

    
db = sqlite3.connect('db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE if not exists MyCourses(CourseID TEXT primary key, CourseName TEXT, CourseGrade int ,studentID TEXT) ''')

try:
    cursor.execute('''INSERT INTO MyCourses values('Math 211','Logic',77,'Fadi')''')
    cursor.execute('''INSERT INTO MyCourses values('EECE 330', 'ProgrammingII',79,'Marwan')''')
    cursor.execute('''INSERT INTO MyCourses values('Math 301','Advanced Differential Eqts',82,'Leen')''') # Save the data in the database
    db.commit()

except:
    print('Not inserted data, already inserted')


printTable(cursor, "MyCourses")


db.close()
del cursor


DBfile = "./db.accdb"
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+ DBfile)
cursorMS = conn.cursor()


printTable(cursorMS, "Names")



DBfile = "./db.accdb"

db = None
MSconnection = None
while(True):
    command = input("Do you want to add an entry to a table (y/n)? ")
    if(command == "n"):
        if(db != None):
            db.close()
            del cursor, db
        if(MSconnection != None):
            MSconnection.close()
        break
    elif(command == "y"):
        if(db == None):
            db = sqlite3.connect('db')
            cursor = db.cursor()
        if(MSconnection == None):
            MSconnection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+ DBfile)
        
        print("\nAvailable Tablesy: \n")
        try:
            cursor.execute('SELECT name FROM sqlite_master WHERE type=\"table\";')
        except Exception as e:
            print(e)
            continue
            
        result = cursor.fetchall()
        for i in result:
            for j in i:
                print("• ", j)
        
        
        command = str(input("\Choose a table: "))
        
        try:
            cursor.execute('select * from '+command+'')
            columns = cursor.description
            sqlstmt = []
           
            tableInfo = cursor.execute('PRAGMA TABLE_INFO('+command+')')
            columnTypes = []
            for i in tableInfo:
                if(i[2] == "TEXT"):
                    columnTypes.append("str")
                if(i[2] == "int"):
                    columnTypes.append("int")
             
            wrongIn = False
            
            for i in range(len(columns)):
                wrong = True
                cmd = ""
                while(wrong == True and cmd != "q"):
                    cmd = input("Enter " + str(columns[i][0]) + ": ")
                    
                    if(columnTypes[i] == "int"):
                        try: 
                            cmd = int(cmd)
                            sqlstmt.append(cmd)
                            wrong = False
                            
                        except:
                            print("Wrong Type of Input, Enter Again (q to quit):")
                            
                            
                    else:
                        try:
                            cmd = int(cmd)
                            print("Wrong Type of Input, Enter Again (q to quit):")
                            
                            
                        except:
                            cmd = str(cmd)
                            sqlstmt.append(cmd)
                            wrong = False
                if(cmd == "q"):
                    wrongIn = True
                    break
                    
            
            
            if(wrongIn == False):
            
                
                exists = False
               
                if(command.lower() == "mycourses"): #only my courses needs to be checked for foreign key currently
                    
                    #This part was done using SQL commands but I was told to do it the "Python way" for some reason
                    #If you want to try it, change initialization of exists to True and comment out the python way
                    '''try:
                        checkSQL = "SELECT * FROM Names WHERE English = \'"+str(sqlstmt[len(sqlstmt)-1])+"\'"
                        MAcursor = MSconnection.execute(checkSQL)
                        present = MAcursor.fetchall()
                        if(present == []):
                            exists = False
                        else:
                            sqlstmt[len(sqlstmt)-1] = sqlstmt[len(sqlstmt)-1].lower().capitalize()
                    except Exception as e:
                        exists = False
                        print(e)'''
                
                    it = cursor.execute('SELECT * FROM MyCourses')
                    tableinfo = cursor.fetchall()
                    
                    for i in tableinfo:
                        if(i[3] == str(sqlstmt[len(sqlstmt)-1].capitalize())):
                            exists = True;
                            break;
                        
                            
                
                
                
                if(exists == True):
                    SQL = "INSERT INTO " + command  + " VALUES("
                    for i in range(len(sqlstmt)):
                        if(i != len(sqlstmt)-1):
                            SQL += "\'" + str(sqlstmt[i]).capitalize() + "\',"
                        else:
                            SQL += "\'" + str(sqlstmt[i]).capitalize() + "\'"
                    
                    SQL += ")"
                
                    columnInfo = cursor.execute('PRAGMA TABLE_INFO(mycourses)')
                    
                    
                    
                    try:
                        
                        cursor.execute(SQL)
                        db.commit()
                        printTable(cursor, command)
                        
                        print("Successfully added\n")
                    except Exception as e:
                        print(e)
                        #print("Course ID is unique, don't use already inserted CourseIDs")
    
                    
                else:
                    print("Student not found, insertion aborted")
            
                
                
                
        except:
            print("Invalid Table")

    else:
        print("Invalid Input, please respond by \"y\" or \"n\"")
    

    






    
    


    
    

