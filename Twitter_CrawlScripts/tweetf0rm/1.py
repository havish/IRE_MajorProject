import os
import json
while(1):
	#f = open("distinctIDs","r")
	#ids= f.readlines()
	#f.close()
 	ids = ['1422889470']
	f1=open("distinctIDs","w")
	i = 0
	while i < range(len(ids)):
		a = str(ids[i])
		command = ("./client.sh -c tests/config.json -cmd CRAWL_FRIENDS -d 2 -dt \"ids\" -uid " + a)
		os.system(command)
		print "./data/friend)ids/" + a
		f = open("./data/friend_ids/" + a)
		for line in f:
			temp = json.loads(line[:-1])
			for j in temp['ids']:
				if j not in ids:
					print j
					f1.write( str(j) + "\n")
		i = i + 1
	break
