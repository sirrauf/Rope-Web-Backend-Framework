sqlcon = Mysql::Client.new('localhost','root','','db_testroperb')
sqlcon = sqlcon.query("CREATE TABLE tb_user(ID_User INT(255) PRIMARY KEY,Name TEXT(),Username VARCHAR(80),Email VARCHAR(20),Password VARCHAR(160)")
puts "Sucessful create table database ^-^\n"
sqlcon.close


