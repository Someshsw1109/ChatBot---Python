import numpy as np
import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

f = open('data.txt', 'r', errors='ignore')
raw_doc = f.read()
raw_doc = raw_doc.lower()
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
sentence_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)
# print(sentence_tokens[:5])
# print(word_tokens[:5])

lemmer = nltk.stem.WordNetLemmatizer()
def LemToken(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormal(text):
    return LemToken(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))

Greet_inp = ('hello', 'hi', 'whassup', 'how are you?')
Greet_resp = ('hi', 'hey', 'Hey There!', 'There there!!')
def Greet(sentence):
    for word in sentence.split():
        if word.lower() in Greet_inp:
            return random.choice(Greet_resp)
        
def Response(user_resp):
    robol_resp = ''
    TfidfVec = TfidfVectorizer(tokenizer= LemNormal, stop_words= 'english')
    tfidf = TfidfVec.fit_transform(sentence_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robol_resp = robol_resp + "Sorry, I'm unable to understand you!"
        return robol_resp
    else:
        robol_resp = robol_resp + sentence_tokens[idx]
        return robol_resp
    
flag = True
print("Hello! I am an AI Bot. Start Typing your text after greeting to talk to me. For ending convo type bye!")
while (flag == True):
    user_resp = input()
    user_resp = user_resp.lower()
    if (user_resp != 'bye'):
        if (user_resp == 'thank you' or user_resp == 'thanks'):
            flag = False
            print('AI Bot: You are welcome.......')
        else:
            if (Greet(user_resp) != None):
                print('AI Bot: ' + Greet(user_resp))
            else:
                sentence_tokens.append(user_resp)
                word_tokens = word_tokens + nltk.word_tokenize(user_resp)
                final_words = list(set(word_tokens))
                print(Response(user_resp))
                sentence_tokens.remove(user_resp)
    else:
        flag = False
        print('AI Bot: Goodbye!')
        