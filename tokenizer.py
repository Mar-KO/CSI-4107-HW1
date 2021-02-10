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



#[MB001, Q0, Tweettime, rank_for_word, score_for_word, tag]

class QueryData(object):
    
    def __init__(self):
        self._query_list = []
    
    def queries(self):
        with open('Queries.txt','r') as f:
            i = 0
            temp_list = []
            for line in f:

                x = line.split() 
                #print(x)
                if (i < 7):
                    temp_list.append(x)
                    i = i + 1
                if (len(temp_list) > 6):
                    cleaned = cleaning(temp_list)
                    temp_list = []
                    self.query_list.append(cleaned)
                    i = -1
  
    # creates an array for every tweet
    def cleaning(self, array):
        temp_list = []
        copy = array
        for line in copy: 
            for word in line:
                if(str(word) == "<num>"):
                    #print(x[2])
                    temp_list.append(line[2])
                if (str(word) == "<querytweettime>"):
                    #print(x[1])
                    temp_list.append(line[1])
                    y=0
                if(str(word) == "<title>"):
                    line.pop(0)
                    line.pop(-1)
                    temp_list.append(line)
                    length = len(line)
        return temp_list
          
 


print(query_list[1])
print(query_list[17])