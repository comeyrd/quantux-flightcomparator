import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
import seaborn as sns

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('universal_tagset')
#nltk.download('vader_lexicon')

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
tokenizer.model_max_length = 512

skyscanner = pd.read_csv("skyskanner.csv")

skyscanner = skyscanner.dropna(subset=['review'])
shortStringCondition = skyscanner['review'].str.len() > 50 #Keeping only the 50 char + strings
skyscanner_long = skyscanner[shortStringCondition]
# Create empty columns to store the outputs
skyscanner_long['roberta_neg'] = ""
skyscanner_long['roberta_neu'] = ""
skyscanner_long['roberta_pos'] = ""


length = len(skyscanner_long)
chunk_size = 10
onepercent = (length/100).__floor__()
print(length)
print(onepercent)
currpercent = 1
for i in range(0,length , chunk_size):
    chunk_tokenized = tokenizer(skyscanner_long["review"].iloc[i:i+chunk_size].tolist(), return_tensors='pt',padding='max_length', truncation=True, max_length=514)
    chunk_modeled = model(**chunk_tokenized)
    skyscanner_long.iloc[i:i+chunk_size, skyscanner_long.columns.get_loc('roberta_neg')] = chunk_modeled.logits[:, 0].detach().numpy()
    skyscanner_long.iloc[i:i+chunk_size, skyscanner_long.columns.get_loc('roberta_neu')] = chunk_modeled.logits[:, 1].detach().numpy()
    skyscanner_long.iloc[i:i+chunk_size, skyscanner_long.columns.get_loc('roberta_pos')] = chunk_modeled.logits[:, 2].detach().numpy()
    if (i / onepercent) > currpercent:
        print(i/onepercent)
        currpercent+=1

skyscanner_long.to_csv('skyskanner_roberted.csv', index=False)