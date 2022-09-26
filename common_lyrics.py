# Esse código resolve algumas daquelas perguntas já...
# a gente pode se basear nele pra fazer o resto
# pena que meu PC não aguenta huehue

import pandas as pd
import matplotlib.pyplot as plt

lyrics_df = pd.read_csv('AMlyrics.csv')
# First, import a csv containing all of the lyrics

#Cleaning the text, removing some words that will get in the way of the analysis.

import string, re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


def remove_punc(lyrics):
    return "".join([c for c in lyrics if c not in string.punctuation])

def remove_stopwords(lyrics):
    return [w for w in lyrics if w not in stopwords.words('english')]

markers = ['[', ']','Verse','1','2','3','Chorus','Spoken Intro','Intro','Bridge','PreChorus', 'and','And','Outro']
def remove_markers(lyrics):
    return [w for w in lyrics if w not in markers]

lyrics = []
tokenizer = RegexpTokenizer(r'\w+')

lyrics_df['lyrics'] = lyrics_df['lyrics'].apply(lambda x: remove_punc(x))
lyrics_df['lyrics'] = lyrics_df['lyrics'].apply(lambda x: tokenizer.tokenize(x))
lyrics_df['lyrics'] = lyrics_df['lyrics'].apply(lambda x: remove_markers(x))
lyrics_df['lyrics'] = lyrics_df['lyrics'].apply(lambda x: remove_stopwords(x))
lyrics_df['lyrics'].head(20)

# Using spacy, we'll see the most frequent words in the lyrics.

lyrics_df['lyrics'] = lyrics_df['lyrics'].apply(lambda x: ' '.join(x))

import spacy
from collections import Counter

def most_freq_words(df, number):
    sp = spacy.load('en_core_web_sm')
    complete_doc = sp(' '.join([i for i in df['lyrics']]))
    words = [token.text for token in complete_doc
             if not token.is_stop and not token.is_punct]
    word_freq = Counter(words)
    common_words = word_freq.most_common(number)
    print (common_words)

# And we'll generate a wordcloud

from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud, STOPWORDS

def word_cloud(df):
    v = TfidfVectorizer()
    x = v.fit_transform(df['lyrics'])
    text = df.lyrics.values
    wordcloud = WordCloud(
        width = 3000,
        height = 2000,
        background_color = 'white',
        stopwords = STOPWORDS).generate(str(text))
    fig = plt.figure(
        figsize = (40, 30),
        facecolor = 'k',
        edgecolor = 'k')
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

# Using all discography, we get the following:

most_freq_words(lyrics_df, 20)

word_cloud(lyrics_df)

# Now, only the 'Suck it and see' album.

sias_df = lyrics_df[lyrics_df['album'] == 'Suck It and See']
most_freq_words(sias_df, 20)
word_cloud(sias_df)

# Now, only the 'TBH&C' album.

tranqulity_df = lyrics_df[lyrics_df['album'] == 'Tranquility Base Hotel & Casino']
most_freq_words(tranqulity_df, 20)
word_cloud(tranqulity_df)


# What topics are more frequent in the lyrics? For what we'll use Latent Dirichlet Allocation

from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

def print_top_words(model, feature_names, n_top_words):
    topics=[]
    for topic_idx, topic in enumerate(model.components_):
        topics.append([feature_names[i]
        for i in topic.argsort()[:-n_top_words - 1:-1]])
    for t in topics:
        print(t)

def lda(tags):
    number_topics = 10
    no_top_words = 5
    no_features = 5000

    ct_vectorizer = CountVectorizer(max_features=no_features)
    tags_ct = ct_vectorizer.fit_transform(tags)

    lda = LatentDirichletAllocation(n_components=number_topics, n_jobs=-1)
    lda.fit(tags_ct)

    ct_features_names = ct_vectorizer.get_feature_names()
    print_top_words(lda, ct_features_names, no_top_words)

# Running it on the whole discography, in the suck it and see and in the tbh&c album

lda(lyrics_df['lyrics'])

lda(sias_df['lyrics'])

lda(tranqulity_df['lyrics'])