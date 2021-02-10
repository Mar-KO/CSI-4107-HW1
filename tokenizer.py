import pandas as pd
import re
from spacy.tokens import Doc
import spacy

stopwords = pd.read_csv("stopwords.txt", names=['stopwords'])
stops =stopwords["stopwords"]
sp = spacy.load("en_core_web_sm")

def Is_StopWord(token):
    ans = False
    for i in stops:
        if (i == str(token)):
            ans = True
    return ans
#print("Answer is:",Is_StopWord("a"))

def Is_Number(token):
    ans = False
    try:
        tmp = int(token)
        #print('The variable is a number')
        return True
    except:
        #print('The variable is not a number')
        return False

def Remove_Punctuations(sentence):
    res = re.sub(r'[^\w\s]', '', sentence)
    return res

def tokenize(*args, **kwrds):
    df = args[0]
    spacy = kwrds['spacy']
    x = Remove_Punctuations(str(df["title"]))
    doc = spacy.tokenizer(x)
    new_token_list = set()
    for token in doc:
        if (Is_StopWord(token.text) == False) and (Is_Number(token.text) == False):
            new_token_list.add(token.lemma_)
    new_doc = Doc(doc.vocab, list(new_token_list))
    return pd.Series({'querytweettime': df["querytweettime"], 'doc': new_doc})

query_list = []
#https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python/16922328
def queries():
    with open('Queries.txt','r') as f:
        
        for line in f:
            temp_list = []
            i = 0
            x = line.split() 
            line_list = []    
            for word in x:
                
                if(str(word) == "<num>"):
                    #print(x[2])
                    temp_list.append(x[2])
                if (str(word) == "<querytweettime>"):
                    #print(x[1])
                    temp_list.append(x[1])
                    y=0
                if(str(word) == "<title>"):
                    x.pop(0)
                    x.pop(-1)
                    length = len(x)
                    #calculate rank for every word in title (for loop needed)
            
            if (len(temp_list) > 0):
                query_list.append(temp_list)
            if (i == 7):
                temp_list = []
            #increment i at every line. Reset Temp_List after 7 lines
            i = i + 1    

        #[MB001, Q0, Tweettime, rank_for_word, score_for_word, tag]

class QueryData(object):
    

    def __init__(self):
        self._hashtable = dict()
        self._documents = dict()

    # document will either be a Series or a DataFrame, 
    # using the tweettime as the key, and the Doc as the value
    def addDocument(self, document):
        self._documents[document['querytweettime']] = document['doc']
          
 

queries()
print(query_list)