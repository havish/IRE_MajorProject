import os
import json
files = os.listdir("./data/friend_ids")
ids = []
output_file = open("./distinctIDs","w")

for f in files:
	temp = open("./data/friend_ids/" + f,"r")
	lines = temp.readlines()
	for i in lines:
		temp1 = json.loads(i)
		for j in temp1["ids"]:
			if(j not in ids):
				ids.append(j)
				output_file.write(str(j) + "\n")
			else:
			 	print j
	temp.close()
