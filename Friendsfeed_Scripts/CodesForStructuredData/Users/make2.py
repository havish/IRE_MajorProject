
#Remove duplicate entires from the user file

users = open("FinalUsers1.csv","r").readlines()
output = open("FinalUsers2.csv","w")
users_dic = {}
for i in users:
    temp = i.split("|")[0]
    try:
        users_dic[temp].append(i)
    except:
        users_dic[temp] = [i]
for i in users_dic:
    output.write(users_dic[i][0])
