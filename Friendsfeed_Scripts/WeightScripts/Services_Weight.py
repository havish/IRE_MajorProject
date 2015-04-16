from collections import Counter

User_Services = {}
Distinct_Servies = {}
with open("./out.csv") as f1:
    for line in f1:
        temp = line[:-1].split("|")
        Distinct_Servies[temp[2]] = 1
        try:
            User_Services[temp[0]].append(temp[2])
        except:
            User_Services[temp[0]] = [temp[2]]


output_file = open("./EdgeServices.csv","w")
Distinct_Servies = Distinct_Servies.keys()
count =0
with open("./FinalFollowing_Swap.csv") as f1:
    for line in f1:
        count += 1
        temp = line[:-1].split("\t")
        userA = temp[0]
        userB = temp[1]
        output_string = userA + "\t" + userB + "\t"
        try:
            User_Services[userA]
            try:
                User_Services[userB]
                Intersection = list((Counter(User_Services[userA]) & Counter(User_Services[userB])).elements())
                Score = float (len(Intersection) / ((len(User_Services[userA]) + len(User_Services[userB]) - len(Intersection)) * 1.0))
                output_string += str(Score) + "\t"
                for ser in Intersection:
                    output_string += ser+","
                output_string = output_string[:-1]
            except:
                output_string += "0.0" + "\t" + "No service subscribed by Second User"
                #print "userB" , "No services"
        except:
            try:
                User_Services[userB]
                output_string += "0.0" + "\t" + "No service subscribed by First User"
            except:
                output_string += "0.0" + "\t" + "No service subscribed by Both Users"
        output_file.write(output_string+"\n")
        if(count % 100000 == 0):
            print count
