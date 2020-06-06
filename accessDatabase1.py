#for alternate login and logout

import pymysql
from datetime import *

def myAddRecord(uname):

    conn = pymysql.connect(host="localhost", user="id13129122_srcbm", 
                           password="RightPaht@123", db="CVproject")
    
    cursor = conn.cursor()
    
    now = datetime.now()
    flag = 1;
    login = 1;
    
    username = uname.lower()
    
    logindate = "{}-{}-{}".format(now.year, now.month, now.day )
    currenttime = "{}:{}:{}".format(now.hour, now.minute, now.second)
    
    #get previous record of the user, if it contains loginTime value
    #then add the new record under LogoutTime value and vice-versa.
    
    #step1. get previous record of the user (DONE)
    cursor.execute("SELECT * FROM staffAttendance where \
                   Username = '{}' ORDER BY AttendanceID DESC LIMIT 1".format(username))
    #if a string is continued in the next line use backslash
    lastRecord = cursor.fetchone();
    #gives a tuple
    
    #step2. check whether record exists or not, 
    #then check whether LoginTime value is present or LogoutTime value is present
    
    if lastRecord is None:
        print("Record of this username doesn't exist")
        flag = 0
    else:
        flag = 1
        if(len(lastRecord[3]) == 0): #if previous record has no LoginTime
            login = 0 #means not logged in
        else:
            login = 1; #means already logged in
        
    #step3. if LoginTime value is present, add the record & current time under LoginTime
    #else add the record and current time under LogoutTime
    
    if(flag == 0):
        cursor.execute("insert into staffAttendance   \
                       (Username, LoginDate, LoginTime) values('{}', '{}', '{}')".  
                       format(username, logindate, currenttime))
        print(username, "'s Record inserted for 1st time successfully under login") 
        #if a string is continued in the next line use backslash
    elif (login == 0):
        cursor.execute("insert into staffAttendance  \
                       (Username, LoginDate, LoginTime) values('{}', '{}', '{}')".
                       format(username, logindate, currenttime))
        print(username, "'s Record inserted successfully under login")
    else:
        cursor.execute("insert into staffAttendance  \
                       (Username, LoginDate, LogoutTime) values('{}', '{}', '{}')".
                       format(username, logindate, currenttime))
        print(username, "'s Record inserted successfully under logout")
        
    conn.commit()
    
    conn.close()

#myAddRecord("bvraju11") #for testing