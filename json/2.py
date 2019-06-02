#-*-coding: utf-8-*-
import json

def loadNames():
	for index in range(len(content["states"])):
		indexes[content["states"][index]["name"].lower()] = index;

def printData(index):
	for data in content["states"][index]:
		print("-"*80);
		print("\n{} : {}\n".format(data, content["states"][index][data]));
		print("-"*80);
if __name__ == '__main__':
	with open("states.json", "r") as j:
		content = json.loads(j.read());
	cmd = "";
	indexes = {};
	loadNames();
	while cmd != "exit":
		cmd =input(">>");
		cmd = cmd.lower()
		if(cmd in indexes):
			printData(indexes[cmd])
		else:
			if(cmd != "exit"):
				print("{} was not found in the file.".format(cmd));
