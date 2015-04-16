import gensim
import os

comments_dic = {}
train_comments = []
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
    def __iter__(self):
        count = 0
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                count += 1
                """if(count%100000 == 0):
                    break """
                yield line.split()


with open("C:\Users\Havish\Desktop\IRE_Project\\friendfeed\Entries\\abc\\commentfinal.csv") as f1:
    for line in f1:
        temp = line[:-1].split("\t")
        user = temp[2]
        comment  = temp[8]
        try:
            comments_dic[user] += comment.split(" ")
        except:
            comments_dic[user] = comment.split(" ")

f1.close()




print len(comments_dic.keys())

sentences = MySentences('C:\Users\Havish\Desktop\IRE_Project\\friendfeed\Entries\\abc') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences,workers=4,min_count = 2)

print "training done"

output_file = open("C:\\Users\\Havish\\Desktop\\IRE_Project\\friendfeed\\Entries\\Comment_contentEdge.csv","w")
count  = 0
with open("C:\Users\Havish\Desktop\IRE_Project\\friendfeed\Entries\\FinalFollowing_Swap.csv") as f1:
    for line in f1:
        temp = line[:-1].split("\t")
        user1 = temp[0]
        user2 = temp[1]
        score = 0.0
        count += 1
        output_string = user1 + "\t" + user2 + "\t"
        try:
            a = comments_dic[user1]
            b = comments_dic[user2]
            try:
                score += model.n_similarity(a,b)
            except:
                score += 0.0
        except:
            print "one of the user didn't post any comments !"
        
        output_string += str(score)
        output_file.write(output_string + "\n")
        if(count % 100000 == 0):
            print count