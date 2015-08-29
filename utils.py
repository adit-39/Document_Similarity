import operator
import math
import pickle
import sys
from preprocessing import process_query
reload(sys)
sys.setdefaultencoding('utf8')

def tfidf(documents,query):
	"""
		TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)
		IDF(t) = log(Total number of documents / Number of documents with term t in it)
		
		Params:
		documents = dictionary where key is index of document in original list, value is list of stemmed terms in document
		query = querie in same format as documents
	"""
	tot_docs = len(documents.keys())
	tfidf_dict = {}
	for index in documents.keys():
		tfidf_dict[index] = 0
		for t in query:
			n = float(documents[index].count(t))/len(documents[index])
			if n!=0:
				c = 0
				for i in documents.values():
					if t in i:
						c+=1
				m = math.log(float(tot_docs)/c)
				tfidf = n*m
				tfidf_dict[index] += tfidf
	
	sorted_tfidf = sorted(tfidf_dict.items(),key=operator.itemgetter(1))
	ret = []
	for i in reversed(sorted_tfidf[-10:]):
		ret.append(i[0])
		#print documents[i[0]]
	return ret
	

if __name__=="__main__":
	docs = pickle.load(open("documents.pkl","rb"))
	q = raw_input("Enter Query: ")
	query = process_query(q)
	top10 = tfidf(docs,query)
	with open("Linear.txt","r") as f:
		text = f.read()
	text = eval(text)
	for i in top10:
		print text[i]
