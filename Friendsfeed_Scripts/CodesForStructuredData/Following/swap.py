
# To change the format of the following file from followedID,followerID,timestamp to followerID,followedID,timestamp


output_file = open("FinalFollowing_Swap.csv","w")
with open("./FinalFollowing.csv") as f1:
    for line in f1:
        temp = line[:-1].split("\t")
        output_string = temp[1] + "\t" + temp[0] + "\t" + temp[2] + "\n"
        output_file.write(output_string)
