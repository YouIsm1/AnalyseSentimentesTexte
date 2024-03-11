import string
from collections import Counter
import matplotlib.pyplot as plt
from textblob import TextBlob
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time

deb=time.time()

ntr=input(" donner la nature de de traitement \n \t soit [(text:1) or (file:2)] : ")

if ntr == "1" :
    text =input(" entrer le text pour traiter : ")
elif ntr == "2" :
    n_f=input(" donner le nom de file txt : ")
    text = open(n_f, encoding="utf-8").read()
else :
    print("you have a error! ")

while ntr != "1" and ntr != "2" :
    ntr = input(" donner la nature de de traitement \n \t soit [(text:1) or (file:2)] : ")

    if ntr == "1":
        text = input(" entrer le text pour traiter : ")
    elif ntr == "2":
        n_f = input(" donner le nom de file txt : ")
        text = open(n_f, encoding="utf-8").read()
    else:
        print("you have a error! ")




text_lower = text.lower()
print("Texte en minuscules : \n", text_lower)

clean_text = text_lower.translate(str.maketrans("", "", string.punctuation))
print("Texte nettoyé : \n", clean_text)

words_list = clean_text.split()
print("Liste des mots : \n", words_list)

nltk.download('stopwords')
from nltk.corpus import stopwords

stop_wor_nltk = set(stopwords.words('english'))


stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

for i in stop_wor_nltk:
    if i not in stop_words:
        stop_words.append(i)

final_words = []
for word in words_list:
    if word not in stop_words:
        final_words.append(word)


print("\nMots effectifs : \n", final_words)

print("\n")

emo_lis=[]
with open('text_emtio.txt',"r") as felemt :
    for var_lin in felemt:
        # print("\nvar_lin : \n",var_lin)
        clr_lin=var_lin.replace("\n","").replace(",","").replace("'","").strip()
         # print("\n clr_lin : \n", clr_lin)
        clean_line = clr_lin.split(":")
        # print("\n clean_line : \n", clean_line)
        if len(clean_line) == 2:
            word, emotion = clean_line

            if word in final_words:
                emo_lis.append(emotion)
                print("\n th word : \t ",word)


print("Liste des émotions : \n", emo_lis)
emotion_count = Counter(emo_lis)
print(emotion_count)




fig, ax1 = plt.subplots()
ax1.bar(emotion_count.keys(), emotion_count.values())
fig.autofmt_xdate()
plt.savefig("graphes/graph.png")
plt.show()
#time.sleep(5) # pause de 5 secondes
plt.close() # fermeture automatique de la fenêtre après la pause


analyzer = SentimentIntensityAnalyzer()
sentiment = analyzer.polarity_scores(text)['compound']
print("polarite depuis SentimentIntensityAnalyzer est : ",sentiment)

blob = TextBlob(text)
sent = blob.sentiment.polarity
print("sent by TextBlob = : ",sent)

if sent>=0.5 :
    print(f" sent : {sent} ,\n emotion : happy")
elif sent<=-0.5 :
    print(f" sent : {sent} ,\n emotion : sad")
elif sent<=0.5 and sent>=-0.5 :
    print(f" sent : {sent} ,\n emotion : nutre")
else :
    print(f" sent : {sent} ,\n emotion : nothing(error) ")

fin=time.time()

print(fin-deb)