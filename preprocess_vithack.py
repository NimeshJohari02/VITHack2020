# Load the pickle file in the preprocess() function at required locations (I've commented those)
# Only use the preprocess function in your program with the message as the parameter. 
# You will be returned a pre-processed file that you can pass to model.predict()

from nltk import pos_tag 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords 
from nltk.corpus import wordnet as wn
import tensorflow as tf 
import pickle


def create_pos(tokenized_list):
    pos_list = []    
    pos_list.extend(pos_tag(tokenized_list)) 
  
    return pos_list 

def filter_message(X): 
    tokenized = []
    for text in X:
        tokens = word_tokenize(text)

        #Filtering only nouns, adjectives and verbs
        temp = []
        for word, pos in create_pos(tokens):   
          if(pos in ['NN','JJ','JJR','JJS','VB','VBD','VBG','VBZ', 'VBN', 'VBP']):
            lemma = wn.morphy(word) 
            if lemma is None:
              temp.append(word)
            else:
              temp.append(lemma) 

        tokenized.append(" ".join(temp)) 
  
    
    return tokenized 

def preprocess(message): 
    message = filter_message(message)

    # pickle.load() <- Directory goes here for tokenizer.pkl 
    t=pickle.load(open('tokenizer.pkl','rb'))
    encoded_docs = t.texts_to_sequences(message)
    X = tf.keras.preprocessing.sequence.pad_sequences(encoded_docs,maxlen= 50 ,padding='post')

    return X 

if __name__ == "__main__":
    from nltk import download 

    download('punkt')
    download('stopwords')
    download('averaged_perceptron_tagger')
    download('maxent_ne_chunker')
    download('words')
    download('wordnet')