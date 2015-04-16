from collections import Counter

User_Likes = {}
with open("./likes.csv") as f1:
    for line in f1:
        temp = line[:-1].split("\t")
        try:
            User_Likes[temp[0]].append(temp[1])
        except:
            User_Likes[temp[0]] = [temp[1]]


output_file = open("./EdgeLikes.csv","w")
count =0
with open("./FinalFollowing.csv") as f1:
    for line in f1:
        count += 1
        temp = line[:-1].split("\t")
        userA = temp[0]
        userB = temp[1]
        output_string = userA + "\t" + userB + "\t"
        try:
            User_Likes[userA]
            try:
                User_Likes[userB]
                Intersection = list((Counter(User_Likes[userA]) & Counter(User_Likes[userB])).elements())
                #print Intersection
                Score = float (len(Intersection) / ((len(User_Likes[userA]) + len(User_Likes[userB]) - len(Intersection)) * 1.0))
                output_string += str(Score)
            except:
                output_string += "0.0" + "\t" + "No Posts liked by User B"
                #print "userB" , "No services"
        except:
            try:
                User_Likes[userB]
                output_string += "0.0" + "\t" + "No Posts liked by First User"
            except:
                output_string += "0.0" + "\t" + "No Posts liked by Both Users"
        #print output_string
        output_file.write(output_string+"\n")

