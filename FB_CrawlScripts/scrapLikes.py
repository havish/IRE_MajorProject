import facebook
import json
import re

def pp(o):
    return json.dumps(o, indent=1)


GX_ACCESS_TOKEN = 'CAACEdEose0cBABekOvD5t5WEOMQdLymWDMViAsm59a0ZAy7pcXickylLuRrjMB6MY7QBWov0AZAvBFZCKLENxuzD9j17vYmo5ayw2sVzCAtAd5Ed5ZBXAZBP6fMUyhb6Xl21C1TYJk62bNK6u5M37ZBwOMV7OqcnMcnrEiZBRu9xbAD0vl6EzyizqLsCbaiskcr5ZBZBOGfZAzaXt2OGDEvwOMf2inALobZCRJdtEc7xwZBwdAZDZD'
gx = facebook.GraphAPI(GX_ACCESS_TOKEN)
#friendFile  = open("/home/prateek/gephi/myfbNetwork.tab",'r')
#friendlist = friendFile.readlines()
friendlist = ['514502418676848']
de = []
for friend in friendlist[1:]:
    try:
        id = friend
        #id = re.split(r'\t+', friend)[0]
        likes = gx.get_connections(str(id),'likes',limit=5000)
        f = open(id,'a')
        f.write(pp(likes))
        f.close()
    except:
        print re.split(r'\t+', friend)[0]
        de.append(id)

def get_groups():
    for friend in friendlist[1:]:
        try:
            id = re.split(r'\t+', friend)[0]
            groups = gx.get_connections(str(id),'groups',limit=5000)
            f = open(id+"_groups",'a')
            f.write(pp(likes))
            f.close()
        except:
            print re.split(r'\t+', friend)[0]
            de.append(id)
