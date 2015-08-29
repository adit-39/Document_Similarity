from nltk import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np
import re

def derive_vocabulary(filename):
	stemmed = []
	text = None
	with open(filename,"r") as f:
		text = f.read()
	text = eval(text)
	documents = {}
	for doc,index in zip(text,range(len(text))):
		query = process_query(doc,False)
		documents[index] = query
	with open('documents.pkl', 'wb') as output:
		pickle.dump(documents, output, pickle.HIGHEST_PROTOCOL)
	return documents

def stopword(word_list):
    filtered_words = [w for w in word_list if not w in stopwords.words('english')]
    return filtered_words


def process_query(query,stem=True):
	st = LancasterStemmer()
	re_tokenizer = RegexpTokenizer('\w+')
	words = re_tokenizer.tokenize(query)
	wnl = WordNetLemmatizer()
	stemmed = []
	if stem :
		for i in words:
			stemmed.append(st.stem(i.decode("utf-8").lower()))
	else:
		for i in words:
			stemmed.append(wnl.lemmatize(i.decode("utf-8").lower()))
	stemmed = stopword(stemmed)
	return stemmed



def text2int(textnum, numwords={}):
	return keywords[textnum]

def append_query(query):
	q = process_query(query,False)
	for word in q:
		try:
			q.append(text2int(word)[0])
		except:
			if word=="boundary":
				if "4" not in q:
					q.append("4")
				if "6" not in q:
					q.append("6")
	return q


if __name__ == '__main__':
	keywords = {}
	keywords["zero"] = ["0","zero"]
	keywords["one"] = ["1","one"]
	keywords["two"] = ["2","two","couple","double"]
	keywords["three"] = ["3","three"]
	keywords["four"] = ["4","four","boundary"]
	keywords["five"] = ["5","five"]
	keywords["six"] = ["6","six","boundary"]
	keywords["couple"] = ["2","two","couple","double"]
	keywords["century"] = ["100","hundred","century","ton"]
	keywords["ton"] = ["100","hundred","century","ton"]
	keywords["double"] = ["2","two","couple","double"]
	with open('lookup.pkl', 'wb') as output:
		pickle.dump(keywords, output, pickle.HIGHEST_PROTOCOL)
	documents = None
	with open("documents.pkl", 'rb') as input:
		documents = pickle.load(input)
	query = raw_input("Enter Query :")
	print append_query(query)