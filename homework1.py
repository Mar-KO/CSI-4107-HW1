# Before starting we will import every module that we will be using
import spacy
import pandas as pd

# The core spacy object that will be used for tokenization, lemmatization, POS Tagging, ...
# Note that this is specifically for the English language and requires the English package to be installed
# via pip to work as intended.

sp = spacy.load("en_core_web_sm")

#read the tweets
df = pd.read_csv("Twitter.txt")
df.head(10)
