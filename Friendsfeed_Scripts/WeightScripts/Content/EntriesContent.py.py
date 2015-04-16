import gensim
import os

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
    def __iter__(self):
        count = 0
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                count += 1
                """if(count%100000 == 0):
                    break"""
                yield line.split()


user_post = {}
with open("C:\\Users\\Havish\\Desktop\\IRE_Project\\friendfeed\\Entries\\EntriesFinal.csv") as f1:
    for line in f1:
        temp = line[:-1].split("\t")
        post = temp[0]
        user = temp[1]
        try:
            user_post[user] += post.split(" ")
        except:
            user_post[user] = post.split(" ")
f1.close()
with open("C:\\Users\\Havish\\Desktop\\IRE_Project\\friendfeed\\Entries\\entriesfinal2.csv") as f1:
    for line in f1:
        temp = line[:-1].split("\t")
        post = temp[0]
        user = temp[1]
        try:
            user_post[user] += post.split(" ")
        except:
            user_post[user] = post.split(" ")
f1.close()
with open("C:\\Users\\Havish\\Desktop\\IRE_Project\\friendfeed\\Entries\\entriesfinal3.csv") as f1:
    for line in f1:
        temp = line[:-1].split("\t")
        post = temp[0]
        user = temp[1]
        try:
            user_post[user] += post.split(" ")
        except:
            user_post[user] = post.split(" ")
f1.close()





sentences = MySentences('C:\\Users\\Havish\\Desktop\\IRE_Project\\friendfeed\\Entries\\def') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences,workers=4,min_count = 2)

print "training done"

output_file = open("C:\\Users\\Havish\\Desktop\\IRE_Project\\friendfeed\\Entries\\Entries_contentEdge.csv","w")
count  = 0
with open("C:\\Users\\Havish\\Desktop\\IRE_Project\\friendfeed\\Entries\\FinalFollowing_Swap.csv") as f1:
    for line in f1:
        temp = line[:-1].split("\t")
        user1 = temp[0]
        user2 = temp[1]
        score = 0.0
        count += 1
        output_string = user1 + "\t" + user2 + "\t"
        try:
            a = user_post[user1]
            b = user_post[user2]
            try:
                score += model.n_similarity(a,b)
            except:
                score += 0.0
        except:
            print "one of the user didn't make any posts !"
        
        output_string += str(score)
        output_file.write(output_string + "\n")
        if(count % 100000 == 0):
            print count