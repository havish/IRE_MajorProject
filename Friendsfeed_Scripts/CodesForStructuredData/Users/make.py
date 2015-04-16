
#remove NULL records from user file
count = 0
output = open("./FinalUsers.csv","w")
with open('./NewUsers.csv') as f1:
    for line in f1:
        temp = line[:-1].split("|")
        if(temp[4] != "null"):
            count += 1
            output.write(line)

print count