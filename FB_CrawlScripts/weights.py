import json
import simplejson
import re
from pprint import pprint
from collections import Counter
from nltk.corpus import stopwords
import facebook

GX_ACCESS_TOKEN = ''
gx = facebook.GraphAPI(GX_ACCESS_TOKEN)

still_de = []
def jaccard(a, b):
	try:
		c = a.intersection(b)
#		print c
	        return float(len(c)) / (len(a) + len(b) - len(c))
	except:
		return 0.0


def pp(o): 
    return json.dumps(o, indent=1)


resultFile = open("weightsOutput",'a')
stopwords = stopwords.words('english')

edgeListFile = open("/home/prateek/gephi/myfbNetwork.gdf",'rw+')
edgelist = edgeListFile.readlines()[52983:]

for edge in edgelist:
	weights=[]
	for x in ["movies","likes","books","music","groups"]:
		print x
		json_likes = [] #json_likes are likes that are returned by gx and are stored, it is in itself a set of dictionaries
		nodes = edge.strip().split(",")
		
		like_category = []
		like_category.append(Counter())	
		like_category.append(Counter())
		for node in nodes :
			try:#if data already scraped and stored in a file.
				f = open("/home/prateek/myfbNetwork/friends"+x+"/"+node,'r')
				data = simplejson.load(f)['data']
				json_likes.append(data)
				f.close()
				#print data
				#print json_likes
				#print "file found for", node

			except:#No file exist, scrap using the fb api, and also write it in a file for further usage.
				try:
					jsonReturned = gx.get_connections(str(id),x,limit=5000)
					json_likes.append(jsonReturned['data'])
					f = open("/home/prateek/myfbNetwork/friends"+x+"/"+node,'w')
					f.write(jsonReturned)
					f.close()
					print "file written for ", node
				except:
					still_de.append(x+":"+node)
					print node,"still an exception or session expired"
		
		#json_likes[0] -> scrapedd likes for f1, ||ly json_likes[1] -> scraped likes for f2.
		print len(json_likes)# should return 2.
		likes = [[],[]] #likes for f1,f2
		i = 0		
		for json in json_likes:
			for dic in json:
				try:
#					like_category[i][dic['category']] += 1
					likes[i].extend(dic['name'].split(" "))
				except:	
					print "a dictionary skipped",dic
			i += 1
		print [len(i) for i in likes]
		#ideally it should split the name and then remove topwords, correct it, we could also use categories if no of likes were too many.
		jkscore = jaccard(set([item for item in likes[0] if item not in stopwords]),set([item for item in likes[1] if item not in stopwords]))
		weights.append(jkscore)
	#concatinate scores for different x's ie movies books etc..        
	weightStr=','.join(str(e) for e in weights)
	#we could take a weighted average too like a[1..N]*weights[1..N], for the time being i have used a[1..N] as 1 for all.
	finalweight = sum(weights)
	line = nodes[0]+","+nodes[1]+","+str(finalweight)+","+weightStr+"\n"
	resultFile.write(line)
	print line

resultFile.close()		
print "still defaulters\n"
f = open("stillDefaulters",'a')
for e in still_de:
	f.write(str(e))
f.close()


