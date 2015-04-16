fo = open("./users.csv", "r+")
out1=open("./NewUsers.csv", "a")
# while (str = fo.readline()!=null):
#     print "Read String is : ", str
# # Close opened file
import nltk

def isEnglish(s):
    try:
        s.decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


for line in fo:
    if isEnglish(line):
        out1.write(line)
    else:
        pass
    
          
    
fo.close()   
out1.close()  