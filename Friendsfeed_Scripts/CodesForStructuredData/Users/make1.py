
#Remove "Group" Records from user file 
count = 0
output = open("FinalUsers1.csv","w")
with open("./FinalUsers.csv") as f:
    for line in f:
        temp = line[:-1].split("|")
        if ( temp[1] == "user"):
            count += 1
            output.write(line)