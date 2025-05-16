
sqlcon = Mysql::Client.new('localhost','root','','')
sqlcon = sqlcon.query("Create database db_testroperb")
puts"Sucessful create database ^-^\n"
sqlcon.close

