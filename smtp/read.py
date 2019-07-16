#-*-coding: utf-8-*-
import imaplib, email
from sys import argv

def main():
	user = argv[1]
	password = argv[2]
	service = "imap.gmail.com"
	conn = imaplib.IMAP4_SSL(service)
	conn.login(user, password)




if __name__ == '__main__':
	main()