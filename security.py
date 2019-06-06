import os, sys

print ("Author : MrViewYT")
print ("Kalau Ngak Tahu Pw Chat Ane")
print ("WhatsApp :+62895377240533")
print ("Telegram : t.me/MrViewYT")
print ("Subscribe Yt Channel MrViewYT")
username = 'MrViewYT'      
password = 'MrViewYTEror404'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "Hello Welcome To My Tools"
			print "Don't Copy My Project !",
			sys.exit()

		else:
			print "Password Kamu Salah!!!"
			print "Back Login"
			restart()

	else:
		print "Username Kamu Salah !!!"
		print "Back Login"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()