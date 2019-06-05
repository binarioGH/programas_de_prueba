#-*-coding: utf-8-*-
import json
from os import path
from sys import argv

def getContent(file):
	if not path.isfile(file):
		with open(file, "w") as f:
			f.write("{}")
	with open(file, "r") as f:
		content = f.read()
	return content
def main():
	content = getContent(argv[1])
	content = json.loads(content)
	cmd = ""
	while cmd != "exit":
		cmd = input(">")
		if cmd[:3] == "set": 
			content[cmd[4:]] = input("Input the value: ");
	content = json.dumps(content, indent=2)
	with open(argv[1], "w") as f:
		f.write(content)

if __name__ == '__main__':
	main()