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

doc = df["title"][1]
doc_sp_1 = sp(doc)

print("a)")
print("")
for token in doc_sp_1.ents:
    print("\"" + token.lemma_)
print("")
