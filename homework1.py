import spacy
import csv
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# The core spacy object that will be used for tokenization, lemmatization, POS Tagging, ...
# Note that this is specifically for the English language and requires the English package to be installed
# via pip to work as intended.

sp = spacy.load("en_core_web_sm")

#read the tweets
df = pd.read_csv("Twitter.csv")
df.head(10)

doc = df["title"]

print("a)")
print(doc)
print("")
my_file = open("tokenized.txt","w+")
for sentence in doc:
    doc_sp_1 = sp(sentence)
    print(sentence)
    for token in doc_sp_1:
        print("\"" + token.lemma_)
        my_file.write(token.lemma_)
print("")


