#-*-coding: utf-8-*-
import json
if __name__ == '__main__':
	jsontxt = '''
	{
	"people":[
	    {
	    "name":"john smith",
	    "phone":"123",
	    "email":"blahblah@gmail.com"
	    },
	    {
	    "name":"jane doe",
	    "phone": "456",
	    "email":"stfu@gmail.com"
	    }
	]
	}
	'''
	data = json.loads(jsontxt);
	d = input(">")
	if(d == "t"):
		print("data: {}\n".format(data));
		print("Type: {}".format(type(data)));
		print("\npersons: {}".format(data["people"]));
	elif(d == "d"):
		newdata = json.dumps(data, indent=2		);
		print(newdata);
	else:
		for info in data["people"]:
			print("\n" + "-"*80 + "\n");
			for dato in info:
				print("{}: {}".format(dato, info[dato]));
			print("\n" + "-"*80 + "\n");