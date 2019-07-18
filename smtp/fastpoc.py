#-*-coding: utf-8-*-
import imaplib
import email

def main():
	user = input("Input your user: ")
	password = input("Input your password: ")
	mail = imaplib.IMAP4_SSL("imap.gmail.com")
	mail.login(user, password)
	subject = input("Input a subject: ")
	mail.select("INBOX")
	result, data = mail.uid("search", None, 'HEADER Subject "{}"'.format(subject))
	print(data)
	mailIDs = data[0].split()
	for ID in mailIDs:
		print(ID)
		result, m = mail.uid("fetch", ID,"(RFC822)")
		m = m[0][1].decode("utf-8")
		raw = email.message_from_string(m)
		print("-"*80)
		print("From:{}\nSubject:".format(raw["From"],raw["Subject"]))
if __name__ == '__main__':
	main()