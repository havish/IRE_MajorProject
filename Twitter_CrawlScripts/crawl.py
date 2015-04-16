import twitter
import time
import os

def twitterpage():    
    CONSUMER_KEY = '72MHkiotkJ1wp6T5QWcSA'
    CONSUMER_SECRET = 'uARrXr52UZB0gTDPWkXENZoyjfQI5lmMu4eNloU'
    OAUTH_TOKEN = '1904683502-R0wHCglhGG2Kz3qZvWkXyqgidU68EzSGEaPD4a5'
    OAUTH_TOKEN_SECRET = 'rnl0NXHuXRi2flIl6qNMH5pcVEbddV89ug4qhsvMJM'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    flag = 0 
    f = open("distinctIDs","r")
    ids = f.readlines()
    counter  = 0
    for i in ids:
	try:
    		statuses = twitter_api.statuses.user_timeline(id = i[:-1])
		os.system("mkdir ./DATA/" + i[:-1])
		output_file = open("./DATA/" + i[:-1] + "/TimeLine_Data","w")
		counter += 1
		for status in statuses:
		  	for j in status:
					if(type(status[j]) == unicode):
						output_file.write("-> " + j.encode('utf8') + "\t" + str(status[j].encode('utf8')) +  "\n")
					else:
						output_file.write("-> " + j.encode('utf8') + "\t" + str(status[j]) +  "\n")
			output_file.write("------------------------------------------------------------------------------------\n")
		print i[:-1] + " - Fetching tweets done !"
	except:
	   	print str(counter) + " Users tweets have been fetched " 
	   	flag = flag +  1
	   	print "flag = " + str(flag)
	    	if(flag % 3 == 1):
    			CONSUMER_KEY = '0d7wxMwV8f4cX3ZbyMyIO1MU9'
    			CONSUMER_SECRET = 'NU7Hl153T22ubEkzg791kx1KYEW5w0AcnPAVH0McPVHTT5F2EE'
    			OAUTH_TOKEN = '124520049-p82XzcH4NnWd7gNEyJKgSl3z7JK3LGyZXhSrNHWV'
    			OAUTH_TOKEN_SECRET = 'OOB8OgdOeEa8avvEJVPPBrgdSCkqtntzqxs9TTHDb0645'
   			auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                	               CONSUMER_KEY, CONSUMER_SECRET)
   			twitter_api = twitter.Twitter(auth=auth)
		elif (flag % 3 == 0):
    			CONSUMER_KEY = '72MHkiotkJ1wp6T5QWcSA'
    			CONSUMER_SECRET = 'uARrXr52UZB0gTDPWkXENZoyjfQI5lmMu4eNloU'
   			OAUTH_TOKEN = '1904683502-R0wHCglhGG2Kz3qZvWkXyqgidU68EzSGEaPD4a5'
    			OAUTH_TOKEN_SECRET = 'rnl0NXHuXRi2flIl6qNMH5pcVEbddV89ug4qhsvMJM'
			auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               			CONSUMER_KEY, CONSUMER_SECRET)
   	 		twitter_api = twitter.Twitter(auth=auth)
		else:
			print "Entered 10 seconds sleep"
			print "USERID when crawling stopped is " + str(i[:-1])
			time.sleep(10)




    """for _ in range(5):
        print "Length of statuses", len(statuses)
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError, e:
            break"""


    """print "--- next_results string ----"
    print next_results
    print "--- End next_results string ----"
    print
    print "--- kwargs string ----"
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
    print kwargs
    print "--- End kwargs string ----"
    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']"""
    
    """brand_name=brandToCheck
    brand_name=brand_name.lower()
    brand_name=brand_name.replace('#','')
    brand_name=brand_name.replace('.','')
    brand_name=brand_name.replace(' ','')
    brand_name=brand_name.replace('\'','')"""
#print str(len(statuses))
#print json.dumps(statuses[0].keys(), indent=1)
    """ Information about search_results:
    Has 2 keys , 'search_metadata' and 'statuses'
    search_results['statuses'] :- List 
    Each item in search_results['statuses'] is a dictionary with following keys:[u'contributors', u'truncated', u'text', u'in_reply_to_status_id', u'id', u'favorite_count', u'source', u'retweeted', u'coordinates', u'entities', u'in_reply_to_screen_name', u'in_reply_to_user_id', u'retweet_count', u'id_str', u'favorited', u'user', u'geo', u'in_reply_to_user_id_str', u'possibly_sensitive', u'lang', u'created_at', u'in_reply_to_status_id_str', u'place', u'metadata']
    """

#-------------------------------------------------------------------------- Insert into mongoDB ------------------------------------------------------


#--------------------------------------------------------------------------- Initialization ---------------------------------------------------------
    """
    user_tweetdata=[]
    brand_tweetdata=[]
    
    
    retweet_count_brand=0
    tweet_count_usermention=0
    retweet_count_usermention=0
    tweet_count_keyword=0
    retweet_count_keyword=0
    tweet_count_hashtag=0
    retweet_count_hashtag=0
    goodtweet_count=0
    badtweet_count=0
    
    
    good_synonyms_set=['good','amazing','awesome','respectable','cool','happening','fantastic','wicked']
    bad_synonyms_set=['ugly','terrible','unsatisfied','bad','sucks','shit','sad','stupid']
    good_synonyms={}
    bad_synonyms={}

#---------------------------------------------------------------------------------------------------------------------------------------------------------

    status_texts = [ status['text'] 
                 for status in statuses ]
    screen_names = [ user_mention['screen_name'] 
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]
    counter = 0
    hashtags = [ hashtag['text'] 
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]


    words = [ w 
          for t in status_texts 
              for w in t.split() ]

	

    objectlist=[]    
    for tag in hashtags:
        if tag.lower() =="levis":
            counter = counter +1    
            objectlist.append(tag)



# Segregation of tweets into user tweets and brand tweets -----------------------------------------------------------


    for i in search_results['statuses']:
    	screen_name=i['user']['screen_name']
	screen_name=screen_name.lower()
	screen_name=screen_name.replace(',','')
	screen_name=screen_name.replace('#','')
	screen_name=screen_name.replace(' ','')
	screen_name=screen_name.replace('_','')
	if(screen_name.find('levis')!=-1):
		brand_tweetdata.append(i)
	else:
		user_tweetdata.append(i)

#----------------------------------------------------------------------------------------------------------------------



#------------------------------Re tweet count for brand tweets ------------------------------------------------------
    for i in brand_tweetdata:
    	retweet_count_brand += int(i['retweet_count'])

#----------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------user tweeets with brand mentioon-------------------------------------
    for status in user_tweetdata:
    	if(brand_name in status['entities']['user_mentions']):
    		tweet_count_usermention += 1
		retweet_count_usermention += int(status['retweet_count'])

#----------------------------------------------------------------------------------------------------------------------

	

#-------------------------------------------------user tweeets with brand keyword-------------------------------------
    for status in user_tweetdata:
    	flag=0
    	word_text=status['text'].split(' ')
	for word in word_text:
		keyword=word.lower()
		keyword=keyword.replace(',','')
		keyword=keyword.replace('#','')
		keyword=keyword.replace('@','')
		keyword=keyword.replace('.','')
		keyword=keyword.replace('-','')
		keyword=keyword.replace(' ','')
		if(keyword.find(brand_name)!=-1):
			flag=1
	if(flag==1):
    		tweet_count_keyword += 1
		retweet_count_keyword += int(status['retweet_count'])

#----------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------- User tweets with brand Hashtag ------------------------------
    for status in user_tweetdata:
    	hashtag_brand='#'+brand_name
	if(status['text'].find(hashtag_brand)!=-1):
		tweet_count_hashtag += 1
		retweet_count_hashtag += int(status['retweet_count'])

#-------------------------------------------------------------------------------------------------------------------------
    	

    retweets = [
                # Store out a tuple of these three values ...
                (status['retweet_count'], 
                 status['retweeted_status']['user']['screen_name'],
                 status['text']) 
                
                # ... for each status ...
                for status in statuses 
                
                # ... so long as the status meets this condition.
                    if status.has_key('retweeted_status')
               ]

    # Slice off the first 5 from the sorted results and display each item in the tuple

# --------------------------------------------------------------------------- Words in Tweets --------------------------------------------------------
    ct=Counter(words)
    ct_list=[]
    for i in ct:
	ct_list.append([i,ct[i]])

    for i in range(len(ct_list)):
	for j in range(len(ct_list)-1):
	    if(ct_list[i][1]>ct_list[j][1]):
		swap=ct_list[i]
		ct_list[i]=ct_list[j]
		ct_list[j]=swap
	
    output=[]
#brand_name='levis'
    count_brandword=0
    for i in range(len(ct_list)):
	d={}
	d['word']=ct_list[i][0]
	d['count']= ct_list[i][1]
	tweet_word=ct_list[i][0].lower()
	tweet_word=tweet_word.replace('#','')
	tweet_word=tweet_word.replace('\'','')
	tweet_word=tweet_word.replace('.','')
	if(tweet_word.find(brand_name)!=-1):
		count_brandword += int(ct_list[i][1])
	output.append(d)
    dic={}
    dic['brand_tweet']=count_brandword
    dic['total_tweet']=len(ct)
#---------------------------------------------------------------   Hash Tags  -----------------------------------------------------------------
    hash_count={}
    for i in hashtags:
    	if i in hash_count:
		hash_count[i] += 1
	else:
		hash_count[i] = 1
    ct_hashtags=Counter(hash_count)
    ct_hashlist=[]
    for i in ct_hashtags:
    	ct_hashlist.append([i,ct_hashtags[i]])

    for i in range(len(ct_hashlist)):
	    for j in range(len(ct_hashlist)-1):
		    if(ct_hashlist[i][1]>ct_hashlist[j][1]):
			    swap=ct_hashlist[i]
			    ct_hashlist[i]=ct_hashlist[j]
			    ct_hashlist[j]=swap
    output_hashtags=[]
    for i in range(len(ct_hashlist)):
    	dic_hash={}
	dic_hash['hash_tag']=ct_hashlist[i][0]
	dic_hash['count']=ct_hashlist[i][1]
	output_hashtags.append(dic_hash)


#------------------------------------------------------------ Sentiment module ----------------------------------------------------------
# respectable , cool , happening , fantastic , wicked
# bad, sucks , shit , stupid  , sad
    for i in good_synonyms_set:
    	good_synonyms[i]=[[i,5]]
    for i in bad_synonyms_set:
    	bad_synonyms[i]=[[i,-5]]


    for i in good_synonyms:	
	synsets = wordnet.synsets( i )
	for synset in synsets:
		for j in synset.lemma_names:
			j=j.replace("_"," ")
			if(j not in good_synonyms[i][0]):
				good_synonyms[i].append([j,5])
    for i in bad_synonyms:
	synsets = wordnet.synsets( i )
	for synset in synsets:
		for j in synset.lemma_names:
			j=j.replace("_"," ")
			if(j not in bad_synonyms[i][0]):
				bad_synonyms[i].append([j,-5])

	


    goodtweets=[]
    badtweets=[]
    for i in user_tweetdata:
    	heuristic_value=0
    	for j in good_synonyms:
		for k in good_synonyms[j]:
			if(i['text'].find(k[0])!=-1):
				heuristic_value += int(k[1])
	for j in bad_synonyms:
		for k in bad_synonyms[j]:
			if(i['text'].find(k[0])!=-1):
				heuristic_value += int(k[1])
	if(heuristic_value>=5):
		goodtweets.append(i['text'])
	elif(heuristic_value<=-5):
		badtweets.append(i['text'])



    goodtweet_count = len(goodtweets)
    badtweet_count = len(badtweets)



#-------------------------------------------------------------------------------- xxxxx --------------------------------------------------------------
		
#------------------------------------------------------------------------------ Print Section ------------------------------------------------------------
	


    for i in statuses[0]:
   	print i+ " : ", statuses[0][i]
	print

    for i in range(len(statuses)):
	    print 'Created at : ' + str(statuses[i]['user']['created_at'])
	    print 'Time zone : ' + str(statuses[i]['user']['time_zone'])
	

    print tweet_count_usermention
    print retweet_count_usermention	
    print tweet_count_keyword
    print retweet_count_keyword	
    print tweet_count_hashtag
    print retweet_count_hashtag	
    print 'Positive Tweets : ',goodtweet_count
    print 'Negative Tweets : ',badtweet_count
    print goodtweets
    print badtweets

#-------------------------------------------------------------------------------- xxxxx ----------------------------------------------------------------------

    return json.dumps({'data':output , 'count':dic , 'hashtags':output_hashtags,'brand_tweetcount':len(brand_tweetdata),'brand_retweetcount': retweet_count_brand,'user_tweetcount':len(user_tweetdata),'keyword_tweetcount':tweet_count_keyword,'keyword_retweetcount':retweet_count_keyword,'mention_tweetcount':tweet_count_usermention,'mention_retweetcount':retweet_count_usermention,'hashtag_tweetcount':tweet_count_hashtag,'hashtag_retweetcount':retweet_count_hashtag, 'goodtweets':goodtweets , 'badtweets':badtweets},indent=1)"""


twitterpage()
