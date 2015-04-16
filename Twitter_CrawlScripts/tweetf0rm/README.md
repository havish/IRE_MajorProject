
*I haven't been updating this for a while, but I just setup a EC2 instance and tested this. Looks like most of the things are still working fine. I have some new research needs myself, so I might update this more frequently in the next few months. But, in general, I would be happy to take requests to add specific functionalities, merge pull requests, and even requests for specific datasets. Just make a ticket ;)*


tweetf0rm
=========

A crawler that helps you collect data from Twitter for research. Most of the heavy works are already done by [Twython](https://github.com/ryanmcgrath/twython). ``tweetf0rm`` is just a collection of python scripts help to deal with parallelization, proxies, and errors such as connection failures. In most use cases, it will auto-restart when an exception occurs. And, when a crawler exceeds the Twitter API's [rate limit](https://dev.twitter.com/docs/rate-limiting/1.1/limits), the crawler will pause itself and auto-restart later.

To workaround Twitter's rate limits, ``tweetf0rm`` can spawn multiple crawlers each with different proxy and twitter dev account on a single computer (or on multiple computers) and collaboratively ``farm`` user tweets and twitter relationship networks (i.e., friends and followers). The communication channel for coordinating among multiple crawlers is built on top of [redis](http://redis.io/) -- a high performance in-memory key-value store. It has its own scheduler that can balance the load of each worker (or worker machines).

It's quite stable for the things that I want to do. I have collected billions of tweets from **2.6 millions** twitter users in about 2 weeks with a single machine.

Dataset
------------
Twitter license (or at least the company's position on this) does not allow me redistribute the crawled data (e.g., someone asked the question a while back: https://dev.twitter.com/discussions/8232). But, here is what I have:

* **Health topics followers**: I crawled **2,686,823** users' tweets (i.e., as of 11/12/2013; maximum of 3,200 per user, limitted by Twitter apis) in a matter of two weeks. All thhese twitter users follow one of the following, what I call, health-related information centers (i.e., person or organization who share health-related information, such as the [CNNHealth](https://twitter.com/cnnhealth). Note that, some of the users either haven't posted anything or have set the privacy setting to private, so it will show zero tweets for these users. Anyway, I haven't done anything to this dataset yet besides doing some pre-processing (indexing, calculate common statistics), although I have some research ideas that I am planning to try. If you want to get a hand on this dataset (either collaborate with me or just want the data), contact me at <ji0ng.bi0n@gmail.com> :). The detailed stats such as how many tweets will be posted as soon as my code gets them calculated (**821,449,519** unique tweets). 
  
  * https://twitter.com/RWJF
  * https://twitter.com/samhsagov
  * https://twitter.com/PublicHealth
  * https://twitter.com/WebMD
  * https://twitter.com/NIMHgov
  * https://twitter.com/HHSGov
  * https://twitter.com/drsanjaygupta
  * https://twitter.com/womenshealth
  * https://twitter.com/HealthHabits
  * https://twitter.com/medlineplus
  * https://twitter.com/KHNews
  * https://twitter.com/NIH
  * https://twitter.com/cnnhealth
  * https://twitter.com/DrOz
  * https://twitter.com/projecthopeorg
  * https://twitter.com/NBCNewsHealth
  * https://twitter.com/LIVESTRONG
  * https://twitter.com/JohnsHopkinsSPH
  * https://twitter.com/CDC_eHealth
  * https://twitter.com/healthfinder
  * https://twitter.com/FamHealthGuide
  * https://twitter.com/AmericanCancer
  * https://twitter.com/HealthCareGov
  * https://twitter.com/goodhealth
  * https://twitter.com/CDCemergency
  * https://twitter.com/Disc_Health
  * https://twitter.com/HarvardHealth
  * https://twitter.com/Health_Affairs
  * https://twitter.com/WomensHealthMag
  * https://twitter.com/latimeshealth
  * https://twitter.com/FDA_Drug_Info
  * https://twitter.com/nytimeshealth
  * https://twitter.com/MayoClinic
  * https://twitter.com/AIDSgov
  * https://twitter.com/NPRHealth
  * https://twitter.com/USDAFoodSafety
  * https://twitter.com/DailyHealthTips
  * https://twitter.com/MinorityHealth
  * https://twitter.com/RedCross
  * https://twitter.com/FDAWomen
  * https://twitter.com/WSJhealth
  * https://twitter.com/runnersworld
  * https://twitter.com/bbchealth
  * https://twitter.com/CMSGov
  * https://twitter.com/AmerMedicalAssn
  * https://twitter.com/KatherineHobson
  * https://twitter.com/MensHealthMag
  * https://twitter.com/FDArecalls
  * https://twitter.com/WSJhealthblog
  * https://twitter.com/CDCgov
  * https://twitter.com/WHO
  * https://twitter.com/GoHealthyPeople
  * https://twitter.com/CDCFlu
  * https://twitter.com/girlshealth

Installation
------------

None... just clone this and start using it. It's not that complicated yet to have a setup.py..

    git clone git://github.com/bianjiang/tweetf0rm.git

Dependencies
------------
To run this, you will need:
- [Twython](https://github.com/ryanmcgrath/twython)
- [futures](https://pypi.python.org/pypi/futures) if you are on Python 2.7
- [redis server](http://redis.io/) and [redis python library](https://pypi.python.org/pypi/redis)
- [requests](http://www.python-requests.org/en/latest/)
- (optional) [lxml](http://lxml.de/) if you want to use the ``crawl_proxies.py`` script to get a list of free proxies from http://spys.ru/en/http-proxy-list/.

##### I haven't tested Python 3 yet... 

Features
------------

- Support running multiple crawler processes (through python ``multiprocessing``) with different proxies on single node;
- Support a cluster of nodes to collaboratively ``f0rm`` tweets.


How to use
------------

First, you'll want to login the twitter dev site and create an applciation at https://dev.twitter.com/apps to have access to the Twitter API!

After you register, create an access token and grab your applications ``Consumer Key``, ``Consumer Secret``, ``Access token`` and ``Access token secret`` from the OAuth tool tab. Put these information into a ``config.json`` under ``apikeys`` (see an example below).

You have to have a redis server setup ([redis quick start](http://redis.io/topics/quickstart)). Note that if you want to run multiple nodes, you will only need to have one redis instance, and that instance has to be reachable from other nodes. The ``redis_config`` needs to be specified in the ``config.json`` as well.

Even you only wants to run on one node with multiple crawler processes, you will still need a local redis server for coordinating the tasks.

		{
			"apikeys": {
				"i0mf0rmer01" :{
					"app_key":"CONSUMER_KEY",
					"app_secret":"CONSUMER_SECRET",
					"oauth_token":"ACCESS_TOKEN",
					"oauth_token_secret":"ACCESS_TOKEN_SECRET"
				},
				"i0mf0rmer02" :{
					"app_key":"CONSUMER_KEY",
					"app_secret":"CONSUMER_SECRET",
					"oauth_token":"ACCESS_TOKEN",
					"oauth_token_secret":"ACCESS_TOKEN_SECRET"
				},
				"i0mf0rmer03" :{
					"app_key":"CONSUMER_KEY",
					"app_secret":"CONSUMER_SECRET",
					"oauth_token":"ACCESS_TOKEN",
					"oauth_token_secret":"ACCESS_TOKEN_SECRET"
				}
			},
			"redis_config": {
				"host": "localhost",
				"port": 6379,
				"db": 0,
				"password": "iloveusm"
			},
			"verbose": "True",
			"output": "./data",
			"archive_output": "./data"
		}

Most of these options are straightforward. ``output`` defines where the crawled data will be stored; ``archive_output`` defines where the gzipped files will be stored (without compression, it takes a lot of space to store the raw tweets; about 100G per 100,000 users tweets).

The proxies need to be listed in ``proxy.json`` file like:

		{
			"proxies": [{"66.35.68.146:8089": "http"}, {"69.197.132.80:7808": "http"}, {"198.56.208.37:8089": "http"}]
		}

The proxy will be verified upon bootstrap, and only the valid ones will be kept and used (currently it's not switching to a different proxy when a proxy server goes down, but will be added soon). There are a lot free proxy servers available.

Remember that Twitter's rate limit is per account as as well as per IP. So, you should have at least one twitter API account per proxy. Ideally, you should more proxies than twitter accounts, so that ``tweetf0rm`` can switch to a different proxy, if one failed (haven't implemented yet, but higher on the list).

To start the ``f0rm", you can simply run:

	
	$ ./bootstrap.sh -c config.json -p proxies.json


To issue a command to the ``f0rm``, you are basically pushing commands to redis. This is how the commands should look like, e.g.,
	
	cmd = {
	 	"cmd": "CRAWL_FRIENDS",
	 	"user_id": 1948122342,
	 	"data_type": "ids",
	 	"depth": 2,
	 	"bucket":"friend_ids"
	}
	
	cmd = {
		"cmd": "CRAWL_FRIENDS",
		"user_id": 1948122342,
		"data_type": "users",
		"depth": 2,
		"bucket":"friends"
	}
	
	cmd = {
		"cmd": "CRAWL_USER_TIMELINE",
		"user_id": 53039176,
		"bucket": "timelines"
	} 

bucket determine where the results will be saved in the ``output`` folder (specified in ``config.json``). All twitter data are json encoded strings, and output files are normally named with the twitter user id, e.g., if you are crawling a user's timeline, all his/her tweets will be organized in the "timelines" sub-folder with his/her twitter id (numerical and unique identifier for each twitter user).

There is a ``client.py`` script that helps you generate these commands and push to the local redis node queue. e.g., 

	$ client.sh -c tests/config.json -cmd CRAWL_FRIENDS -d 1 -dt "ids" -uid 1948122342

means you want to crawl all friends of ``uid=1948122342`` with ``depth`` as ``1`` and the results are just the twitter user ids of his/her friends. There are also commands you can use to crawl a list of users, e.g., 
	
	$ client.sh -c tests/config.json -cmd BATCH_CRAWL_FRIENDS -d 1 -dt "ids" -j user_ids.json

instead of providing a specific ``user_id``, you provide a ``json`` file that contains a list of ``user_ids``.

MISC
------------

There is also a script (``scripts/crawl_proxies.py``) for crawling proxies server list from spy.ru. It will crawl the http proxies listed in spy.ru, test each one and produce the ``proxies.json`` with valid proxies.

Note that, if you don't use proxies, you can only have one crawler active, since Twitter's rate limit applies to both the account as well as the IP.


### License
------------

The MIT License (MIT)
Copyright (c) 2013 Jiang Bian (ji0ng.bi0n@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/bianjiang/tweetf0rm/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

