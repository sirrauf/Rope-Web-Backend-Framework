import mysql.connector
import os
import requests,json

print("==========================================================================================\n")
print("Welcome to Rope backend web framework ^-^\n")
nameapp = "Rope backend web framework\n"
version = "Version 2.0\n"
devby = "Ananda Rauf Maududi\n"
print(nameapp)
print(version)
print("Developed by:",devby)
print("==========================================================================================\n")
class MenuRope():
  def MenuRope():
      print("Menu Rope web framework backend:\n")
      print
      print("1.Rope Python create database")
      print("2.Rope Python connect database")
      print("3.Rope Python create table database")
      print("4.Rope Python insert data to database")
      print("5.Rope Python rest api")
      print("6.Rope Python cloud devops")
      print("7.Rope Ruby create web app using Ruby on Rails")
      print("8.Rope Ruby create database")
      print("9.Rope Ruby connect database")
      print("10.Rope Ruby create table database")
      print("11. Rope Ruby insert data to database")
      print("12.Rope Ruby rest api")
      print("13.Rope Ruby cloud devops\n")
class Ropepy:
  def createdb(self):
       #Create Database Python
        dbcon = mysql.connector.connect(host="localhost",user="root",passwd="")
        createdb = dbcon.cursor()
        createdb.execute("CREATE DATABASE db_testrope")
        print("Sucessful create database ^-^\n")
        
  def condb(self):      
        #Connect database Python 
        dbcon = mysql.connector.connect(host="localhost",user="root",passwd="",database="db_testrope")
        if dbcon.is_connected():
         print("Sucessful connected database ^-^\n")
     
        
  def createtb(self):
         #Create table Database Python
        dbcon = mysql.connector.connect(host="localhost",user="root",passwd="",database="db_testrope")
        createtable = dbcon.cursor()
        sql = "CREATE TABLE tb_user(ID_User INT(255) NOT NULL PRIMARY KEY AUTO_INCREMENT,Name TEXT NOT NULL,Username VARCHAR(80) NOT NULL,Email VARCHAR(20) NOT NULL,Password VARCHAR(160)NOT NULL)"
        createtable.execute(sql)
        print("Sucessful create table database ^-^\n")
  def insertdatasqlPY(self):
       #Insert into SQL Python
        dbcon = mysql.connector.connect(host="localhost",user="root",passwd="",database="db_testrope")
        createtable = dbcon.cursor()
        sql = "INSERT INTO tb_user(ID_User,Name,Username,Email,Password)VALUES('1','Ananda Rauf Maududi','anandarauf02','anandarauf02@gmail.com,'testpassword123')"
        createtable.execute(sql)
        print("Sucessful insert data to database ^-^\n")
  def restapiPy(self):
        #Rest API Python
        Client_ID =""
        Client_Secret = ""
        token_url =""
        api_url = ""
        data= {'grant_type':'client_credentials'}
        responce = requests.post(token_url,data=data,verify=False,allow_redirects=False, auth=(Client_ID,Client_Secret))
        print(responce.headers)
        print(responce.text)
        tokens = json.loads(responce.text)
        print("You have access token"+tokens['access_token'])
        call_api_headers = {'Authorization':'Bearer'+tokens['access_token']}
        call_api_responce = requests.get(api_url, headers=call_api_headers,verify=False)
        print (call_api_responce.text)
        print ("Succesful connect api")
  def clouddevopsPy(self):
        #Cloud Devops Python
        print("Please,fullfill syntax rest api by yourself ^-^\n")

class Roperb:   
  def createapp(self):
        #Create app web by using Ruby on rails 
        os.system("Ror.bat")
        os.system("Ror.bat > outrails.txt")
        print("Successful create web app on Ruby on Rails ^-^\n")
        
  def createdbRb(self):
        #Create database Ruby
        os.system("createdb.rb")
        os.system("createdb.rb > outputruby.txt")
        print("Successful create database ^-^\n")   
  def condbRb(self):
        #Connect database Ruby
        
        os.system("conndb.rb")
        os.system("conndb.rb > outputruby.txt") 
        print("Successful connect database ^-^\n")
  def createtbRb(self):      
        #Create table
        
        os.system("createtb.rb")
        os.system("createtb.rb > outputruby.txt")
        print("Successful create table database ^-^\n")
  def insertdataRb(self):
      #Insert into SQL Rope Ruby
        os.system("insertdata.rb")
        os.system("insertdata.rb > outputruby.txt")
        print("Successful insert data to database ^-^\n")
  def restapiRb(self):
        #RestAPiRuby
        os.system("restapi.rb")
        os.system("restapi.rb > outputruby.txt")
        print("Please,fullfill syntax by yourself ^-^\n")
  
  def clouddevopsRb(self):
        #RestAPiRuby
        os.system("cloud-devops.rb")
        os.system("restapi.rb > outputruby.txt")
        print("Please,fullfill syntax by yourself ^-^\n")

MenuRope.MenuRope()

ch = int(input("Please,choose number on menu:"))
RopePY = Ropepy()
RopeRB = Roperb()
if ch== 1:
        RopePY.createdb()
elif ch==2:
        RopePY.condb()
elif ch==3:
        RopePY.createtb()
elif ch==4:
    RopePY.insertdatasqlPY()
elif ch==5:
        RopePY.restapiPy()
elif ch==6:
        RopePY.clouddevopsPy
elif ch==7:
        RopeRB.createapp()
elif ch==8:
        RopeRB.createdbRb()
elif ch==9:
        RopeRB.condbRb()
elif ch==10:
        RopeRB.createtbRb()
elif ch==11:
    RopeRB.insertdataRb()
elif ch==12:
        RopeRB.restapiRb()
elif ch==13:
        RopeRB.clouddevopsRb()
else:
        exit
