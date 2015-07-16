from __future__ import division
import re, math
from collections import Counter
from nltk import corpus,word_tokenize,Text
from nltk.corpus import wordnet,stopwords

WORD = re.compile(r'\w+')
global text_vocab1
global text_vocab2
global dictionary
global count_cosine
def ConvertToTextObj(string):
    #global text
    #f = open(filename,'rU')

    #Read the file in string format
    #raw = f.read()
    #Tokenize the words using words (Listing them out)
    tokens = word_tokenize(string)
    #Converting the text file into Nltk Object Text
    text = Text(tokens)
    return text


def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)









def TextVocabulary(text):
    #Return Text words present in the Text
    return set(w.lower() for w in text if w.isalpha())

def EnglishVocabulary():
    #Return English Vocab words stored in NLTK
    return set(w.lower() for w in corpus.words.words())

def StopWords():
    return set(stopwords.words('english'))

def UnusualWords(text_vocab,text):
    #Return Unusual words in the Text provided
    #print text_vocab
    eng_vocab = EnglishVocabulary()
    return sorted(text_vocab-eng_vocab)






def find_synonyms(text_vocab2):
    #global text_vocab2
    global dictionary
    dictionary = {}
    text_vocab = text_vocab2 - StopWords()
    print text_vocab
    for words in text_vocab:
        x = list(wordnet.synsets(words))
        #list_syn = [str(x[i]).split("'")[1].split('.')[0] for i in xrange(len(x))]
        list_syn = []
        for i in xrange(len(x)):
            a = str(x[i]).split("'")[1].split('.')[0]
            list_syn.append(a)
        dictionary[words] = list(set(list_syn))
        #return list_syn
    return dictionary

def findmaxcosine(sentence_student,sentences1):
    values = []
    for lines in sentences1:
    	print sentence_student
    	print lines
    	cosine = get_cosine(text_to_vector(sentence_student),text_to_vector(lines))
    	print cosine
    	values.append(cosine)
    return max(values)


def FinalCheck(v1,v2):
	#global count_cosine
	global text_vocab2

   	count_cosine = []
   	sentences1 = v1.split(".")
   	if len(sentences1)>1:
   	   	for sen in xrange(1,len(sentences1)):
   			sentences1[sen] = sentences1[sen][1:]
   		sentences1 = sentences1[:-1]
   	sentences2 = v2.split(".")
   	if len(sentences2)>1:
   		for sen in xrange(1,len(sentences2)):
			sentences2[sen] = sentences2[sen][1:]
		sentences2 = sentences2[:-1]
	
	# list_of_words = []
	# for line in sentences1:
	# 	x = line.split(" ")
	# 	for word in x:
	# 		list_of_words.append(word)	
	# print list_of_words
	print find_synonyms(text_vocab2)




    


   	#print sentences2    
   	for sentence in sentences2:
   		count_cosine.append(findmaxcosine(sentence,sentences1))
	print count_cosine

def main():
    #vector1 = text_to_vector(raw_input("Enter the first sentence:\n>"))
    #vector2 = text_to_vector(raw_input("Enter the second sentence:\n>"))
    #cosine = get_cosine(vector1, vector2)
    #print 'Cosine:', cosine
    #find_synonyms('dog')
    global text_vocab2
    global dictionary
    marks = 0
    
    #totalmarks = input("Enter the marks to be given for the specific answer:\n>")
    
    #Inputs
    #file1 = raw_input("Enter the model answer:\n>")
    #file2 = raw_input("Enter the student's answer:\n>")
    v3 = [str(i) for i in raw_input("Enter the keywords needed seperated by commas:\n>").split(',')]
    v3 = set(v3)

    with open ("ans.txt", "r") as myfile:
        v1 = myfile.readlines()
    myfile.close()    
    with open ("new.txt", "r") as myfile:
        v2 = myfile.readlines()
    myfile.close()
    v1 = ''.join(v1)
    v2 = ''.join(v2)

    ind = []
    
    sw_list = list(StopWords())
    hey = v2.split(".")
    count = 0
    for line in hey:
		num_thresh = 0
		den_thresh = 0
		a = line.split(" ")
		for word in a:
			if word in sw_list:
				num_thresh+=1		
			den_thresh+=1
		print num_thresh
		print den_thresh	
		print num_thresh/den_thresh
		ind.append(num_thresh/den_thresh)
    print "hello"   
    count = 0
    
    for no in ind:
    	if no<0.19:
	    hey.pop(ind.index(no))
    if str(hey[0])[1]==' ':
        hey[0] = str(hey[0])[1:]    
    v2 = ''.join(hey)
    print v2    

    #Convert into NLTK objects
    text2 = ConvertToTextObj(v2)
    text1 = ConvertToTextObj(v1)
    #print text1
    #print str(text1)

    #Find Word Lists
    text_vocab1 = TextVocabulary(text1)
    text_vocab2 = TextVocabulary(text2)
    

    FinalCheck(v1,v2) 
    #Find Unusual Keywords
    keyw1 = UnusualWords(text_vocab1,text1)
    keyw2 = UnusualWords(text_vocab2,text2)
    #print type(keyw1)





    #1.5 Mark for the occurence of non keywords and unusual words
    templist = [str(i).lower() for i in v3]
    nonkeyunusual = set(keyw1)-set(templist)
    nku = []
    for words in nonkeyunusual:
    	try:
            nku.append(v2.lower().count(words)/v1.lower().count(words))
        except:
            nku.append(0)
    count = 0
    for counting in nku:
    	count+=counting
    #print len(nku)
    
    if len(nku)==0:
        if v1==v2:
            marks=1.5
        else:
            marks=1    
    else:
        count = count*100/len(nku)	
        marks += count*1.5/100
    print "Out of 1.5 Marks: "+str(marks)
    #3.5 Marks for the occurence of keywords mentioned
    impkw = []
    for words in v3:
        try:
    	   impkw.append(v2.lower().count(words.lower())/v1.lower().count(words.lower()))
        except:
            impkw.append(0)
    count = 0
    for counting in impkw:
    	count+=counting
    print count    
    count = count*100/len(impkw)
    marks += count*3.5/100	


    print "Out of 5 Marks "+str(marks)




    #find_synonyms(text_vocab1,list(v2.split(" ")))




    #print UnusualWords(text)







if __name__ == '__main__':
    main()    
