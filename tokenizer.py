import pandas as pd
import re
from spacy.tokens import Doc

stopwords = pd.read_csv("stopwords.txt", names=['stopwords'])
stops =stopwords["stopwords"]

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
    # x = Remove_Punctuations(str(df["title"]))
    x = str(df['title'])
    doc = spacy(x)
    new_token_list = list()
    for token in doc:
        if not(token.is_stop == True or token.like_num == True or token.is_punct == True or token.like_url == True):
            new_token_list.append(token.lemma_)
    new_doc = Doc(doc.vocab, new_token_list)
    return pd.Series({'querytweettime': df["querytweettime"], 'doc': new_doc})
