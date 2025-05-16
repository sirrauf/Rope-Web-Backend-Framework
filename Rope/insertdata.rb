@db_host = "localhost"
@db_user = "root"
@db_pass = ""
@db_name = "db_testroperb"
sqlcon = Mysql::Client.new(:host=>@db_host, :username=>@db_user, :password=>@db_pass, :database=>@db_name)
@result = sqlcon.query("INSERT INTO tb_user(ID_user,Name,Username,Email,Password)VALUES('NULL','Ananda Rauf Maududi','anandarauf02','anandarauf02@gmail.com','testpassword123')")
puts "Sucessful insert data to database ^-^\n"
puts sqlcon
sqlcon.close