# Text processing
#The script removes the first tokenizes the content , then removes the stop words and then saves the root form of the words in another file

import nltk
from nltk.corpus import stopwords
import re
from nltk import PorterStemmer


regex = re.compile(r'\d+\.?\d+|[a-zA-Z0-9]+')

words = ["a","aaa", "able", "about", "above", "according",
         "accordingly", "across", "actually", "after", "afterwards",
         "again", "against", "all", "allow", "allows", "almost", "alone",
         "along", "already", "also", "although", "always", "am", "among",
         "amongst", "an", "and", "another", "any", "anybody", "anyhow",
         "anyone", "anything", "anyway", "anyways", "anywhere", "apart",
         "appear", "appreciate", "appropriate", "are", "around", "as",
         "aside", "ask", "asking", "associated", "at", "available", "away",
         "awfully", "bbb", "be", "became", "because", "become", "becomes",
         "becoming", "been", "before", "beforehand", "behind", "being",
         "believe", "below", "beside", "besides", "best", "better",
         "between", "beyond", "both", "brief", "but", "by", "ccc", "came",
         "can", "cannot", "cant", "cause", "causes", "certain", "certainly",
         "changes", "clearly", "co", "com", "come", "comes", "concerning",
         "consequently", "consider", "considering", "contain", "containing",
         "contains", "corresponding", "could", "course", "currently", "ddd",
         "definitely", "described", "despite", "did", "different", "do",
         "does", "doing", "done", "down", "downwards", "during", "eee",
         "each", "edu", "eg", "eight", "either", "else", "elsewhere",
         "enough", "entirely", "especially", "et", "etc", "even", "ever",
         "every", "everybody", "everyone", "everything", "everywhere", "ex",
         "exactly", "example", "except", "fff", "far", "few", "fifth",
         "first", "five", "followed", "following", "follows", "for",
         "former", "formerly", "forth", "four", "from", "further",
         "furthermore", "ggg", "get", "gets", "getting", "given", "gives",
         "go", "goes", "going", "gone", "got", "gotten", "greetings", "hhh",
         "had", "happens", "hardly", "has", "have", "having", "he", "hello",
         "help", "hence", "her", "here", "hereafter", "hereby", "herein",
         "hereupon", "hers", "herself", "hi", "him", "himself", "his",
         "hither", "hopefully", "how", "howbeit", "however", "iii", "ie",
         "if", "ignored", "immediate", "in", "inasmuch", "inc", "indeed",
         "indicate", "indicated", "indicates", "inner", "insofar",
         "instead", "into", "inward", "is", "it", "its", "itself", "jjj",
         "just", "kkk", "keep", "keeps", "kept", "know", "knows", "known",
         "lll", "last", "lately", "later", "latter", "latterly", "least",
         "less", "lest", "let", "like", "liked", "likely", "little", "ll",
         "look", "looking", "looks", "ltd", "mmm", "mainly", "many", "may",
         "maybe", "me", "mean", "meanwhile", "merely", "might", "more",
         "moreover", "most", "mostly", "much", "must", "my", "myself",
         "nnn", "name", "namely", "nd", "near", "nearly", "necessary",
         "need", "needs", "neither", "never", "nevertheless", "new", "next",
         "nine", "no", "nobody", "non", "none", "noone", "nor", "normally",
         "not", "nothing", "novel", "now", "nowhere", "nno", "obviously",
         "of", "off", "often", "oh", "ok", "okay", "old", "on", "once",
         "one", "ones", "only", "onto", "or", "other", "others",
         "otherwise", "ought", "our", "ours", "ourselves", "out", "outside",
         "over", "overall", "own", "ppp", "particular", "particularly",
         "per", "perhaps", "placed", "please", "plus", "possible",
         "presumably", "probably", "provides", "qqq", "que", "quite", "qv",
         "rrr", "rather", "rd", "re", "really", "reasonably", "regarding",
         "regardless", "regards", "relatively", "respectively", "right",
         "sss", "said", "same", "saw", "say", "saying", "says", "second",
         "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems",
         "seen", "self", "selves", "sensible", "sent", "serious",
         "seriously", "seven", "several", "shall", "she", "should", "since",
         "six", "so", "some", "somebody", "somehow", "someone", "something",
         "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry",
         "specified", "specify", "specifying", "still", "sub", "such",
         "sup", "sure", "ttt", "take", "taken", "tell", "tends", "th",
         "than", "thank", "thanks", "thanx", "that", "thats", "the",
         "their", "theirs", "them", "themselves", "then", "thence", "there",
         "thereafter", "thereby", "therefore", "therein", "theres",
         "thereupon", "these", "they", "think", "third", "this", "thorough",
         "thoroughly", "those", "though", "three", "through", "throughout",
         "thru", "thus", "to", "together", "too", "took", "toward",
         "towards", "tried", "tries", "truly", "try", "trying", "twice",
         "two", "uuu", "un", "under", "unfortunately", "unless", "unlikely",
         "until", "unto", "up", "upon", "us", "use", "used", "useful",
         "uses", "using", "usually", "uucp", "vvv", "value", "various",
         "ve", "very", "via", "viz", "vs", "www", "want", "wants", "was",
         "way", "we", "welcome", "well", "went", "were", "what", "whatever",
         "when", "whence", "whenever", "where", "whereafter", "whereas",
         "whereby", "wherein", "whereupon", "wherever", "whether", "which",
         "while", "whither", "who", "whoever", "whole", "whom", "whose",
         "why", "will", "willing", "wish", "with", "within", "without",
         "wonder", "would", "would", "xxx", "yyy", "yes", "yet", "you",
         "your", "yours", "yourself", "yourselves", "zzz", "zero","the"]
stopwords = {}
for i in words:
    stopwords[i] = 1

output_file = open("./EntriesFinal.csv","w")
count = 0
with open("./entries1out2.csv") as f1:
    for line in f1:
        count += 1
        if(count % 100000 == 0):
            print count

        temp1 = line[:-1].split("\t")
        temp = temp1[7].split(" ")
        filtered_words = []
        #---------------------------------------------- Removing stop words ------------------------------#
        for w in temp:
            s = w
            try:
                stopwords[s]
            except:
                filtered_words.append(s)
            #-------------------------------------------------------------------------------------------------#
        final_line = ""
        for word in filtered_words:
            s = PorterStemmer().stem_word(word) # Obtaining the root form of the token
            final_line = final_line + s + " "
        output_line = ""
        for i in range(11):
            if(i != 7):
                output_line += temp1[i] + "\t"
            else:
                output_line += final_line + "\t"
        output_line += temp1[11]
        #print line[:-1]
        #print output_line
        output_file.write(output_line + "\n")