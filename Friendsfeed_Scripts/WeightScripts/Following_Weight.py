import operator
from collections import Counter
user_dic = {}
following = {}
with open("./FinalFollowing_Swap.csv") as f1:
    for line in f1:
        temp = line[:-1].split("\t")
        user1 = temp[0]
        user2 = temp[1]

        try:
            user_dic[user2] += 1
        except:
            user_dic[user2] = 1

        try:
            following[user1].append(user2)
        except:
            following[user1] = [user2]


user_dic = sorted(user_dic.items(), key=operator.itemgetter(1),reverse = True)


user_dic = user_dic[:1000]
top_following = {}
for i in user_dic:
    top_following[i[0]] = 1


output_file = open("./PopularEdge.csv","w")
with open("./FinalFollowing_Swap.csv") as f1:
    for line in f1:
        output_string = ""
        temp = line[:-1].split("\t")
        user1 = temp[0]
        user2 = temp[1]

        output_string = user1 + "\t" + user2 + "\t"

        following_u1 = []
        following_u2 = []

        for u in following[user1]:
            try:
                top_following[u]
                following_u1.append(u)
            except:
                b = 1
        try:
            for u in following[user2]:
                try:
                    top_following[u]
                    following_u2.append(u)
                except:
                    b = 1
        except:
            following_u2 = []

        Intersection = list((Counter(following_u1) & Counter(following_u2)).elements())
        try:
            score = len(Intersection) / ((len(following_u1) + len(following_u2) - len(Intersection)) * 1.0)
        except:
            score = 0.0

        output_string = str(score)

        output_file.write(output_string + "\n")

        #print score

