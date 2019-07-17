#-*-coding: utf-8-*-
import email, imaplib

def main():
	user = input("Input your email: ")
	password = input("Input your password: ")
	try:
		mail = imaplib.IMAP4_SSL("imap.gmail.com")
		mail.login(user, password)
	except Exception as e:
		print(e)
		exit()
	mail.select("INBOX")
	result,data = mail.uid("search", None, "ALL")
	oldest = data[0].split()[-1]
	result, bytemail = mail.uid("fetch", oldest, "(RFC822)")
	raw_email = bytemail[0][1].decode("utf-8")
	recv = email.message_from_string(raw_email)
	print("To: {}\nFrom: {}\nSubject: {}".format(recv["To"], recv["From"], recv["Subject"]))



if __name__ == '__main__':
	main()