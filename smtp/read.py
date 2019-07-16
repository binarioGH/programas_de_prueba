#-*-coding: utf-8-*-
import imaplib, email
from sys import argv

def main():
	user = argv[1]
	password = argv[2]
	service = "imap.gmail.com"
	conn = imaplib.IMAP4_SSL(service)
	conn.login(user, password)
	conn.select("INBOX")
	newdir = input("Enter the name of the new item: ")
	conn.create(newdir)
	conn.list()
	result, data = mail.uid("search", None, "ALL")
	





if __name__ == '__main__':
	main()