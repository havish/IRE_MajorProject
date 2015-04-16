# This Script retains only those edges in the following file which connect users 'a' and 'b' such that both users are present in the users file

import operator
users = open("60000Users.csv","r").readlines()
users_dic = {}
#user_data = {}
for i in users:
    temp = i.split("|")[0]
    users_dic[temp] = 0
    #user_data[temp] = i


count  = 0
line_count = 0
output = open("FinalFollowing.csv", "w")
with open("./followingAugSept.csv") as f1:
    for line in f1:
        line_count += 1
        if(line_count % 1000000 == 0):
            print line_count
        temp = line[:-1].split("\t")
        try:
            users_dic[temp[0]] += 1
            users_dic[temp[1]] += 1
            output.write(line)
            count += 1
        except:
            b = 1
print count



"""user_dic = sorted(users_dic.items(), key=operator.itemgetter(1),reverse = True)
o = open("60000Users.csv","w")
count = 0
for i in user_dic:
    o.write(user_data[i[0]])
    count += 1
    if(count % 60000 == 0):
        break """
