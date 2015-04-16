from collections import Counter

user_post = {}
count =0
with open("./EntriesFinal.csv") as f1:
    for line in f1:
        count += 1
        temp = line[:-1].split("\t")
        post = temp[0]
        user = temp[1]
        try:
            user_post[user].append(post)
        except:
            user_post[user] = [post]
f1.close()
with open("./entriesfinal2.csv") as f1:
    for line in f1:
        count += 1
        temp = line[:-1].split("\t")
        post = temp[0]
        user = temp[1]
        try:
            user_post[user].append(post)
        except:
            user_post[user] = [post]
f1.close()
with open("./entriesfinal3.csv") as f1:
    for line in f1:
        count += 1
        temp = line[:-1].split("\t")
        post = temp[0]
        user = temp[1]
        try:
            user_post[user].append(post)
        except:
            user_post[user] = [post]
f1.close()

user_likepost = {}
with open("./likes.csv") as f1:
    for line in f1:
        temp = line[:-1].split("\t")
        user = temp[0]
        post = temp[1]
        try:
            user_likepost[user].append(post)
        except:
            user_likepost[user] = [post]

f1.close()


print "done"
count = 0
output_file = open("LikesEdgefile","w")
with open("./FinalFollowing_Swap.csv") as f1:
    for line in f1:
        temp = line[:-1].split("\t")
        user1 = temp[0]
        user2 = temp[1]
        output_string = user1 + "\t" + user2 + "\t"
        #print user1,user2
        try:
            user_likepost[user1]
            user_post[user2]
            user_likepost[user2]
            user_post[user1]
            Intersection1 = list((Counter(user_likepost[user1]) & Counter(user_post[user2])).elements())
            Intersection2 = list((Counter(user_likepost[user2]) & Counter(user_post[user1])).elements())
            score = ( len(Intersection1) / (len(user_likepost[user1]) * 1.0) ) + ( len(Intersection2) / (len(user_likepost[user2])*1.0) )
            output_string += str(score)
            count += 1
            #print user1
            #user_post[user2]
        except:
            output_string += "0.0"
        output_file.write(output_string + "\n")

print count