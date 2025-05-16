require "mysql"
@db_host = "localhost"
@db_user = "root"
@db_pass = ""
@db_name = "db_testroperb"
sqlcon = Mysql::Client.new(:host=>@db_host, :username=>@db_user, :password=>@db_pass, :database=>@db_name)
puts "Sucessful connect database ^-^\n"
puts sqlcon
sqlcon.close