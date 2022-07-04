##################################################
import re
import nltk
import difflib
import os
import math
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from textblob import TextBlob
from operator import itemgetter

nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('omw-1.4')
nltk.download('brown')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
porter_stemmer = PorterStemmer()
lmtzr = WordNetLemmatizer()
###################################################
def preprocess_text(text):
    # lowercase
    text = text.lower()
    text = text.strip()
    
    #remove tags
    #text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    
    # remove special characters and digits
    #text=re.sub("(\\d|\\W)+"," ",text)
    #new_text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    #text=re.sub('[^A-Za-z0-9_-]+', ' ', text)
    text = re.sub('[^A-Za-z ]+', '', text)
    
    ##Convert to list from string
    text = text.split()
    #Tokenize
    #text = word_tokenize(text)

    # remove words less than three letters
    text = [word for word in text if len(word) >= 3]

    # remove stopwords
    text = [word for word in text if word not in stop_words]

    # lemmatize
    text = [lmtzr.lemmatize(word) for word in text]

    # stemming
    #text = [porter_stemmer.stem(word) for word in text]
    
    return ' '.join(text)

# Clean the basic keywords and remove the spaces and noise
def clean_orginal_kw(orginal_kw):
    orginal_kw_clean =[]
    for doc_kw in orginal_kw:
        tt = preprocess_text(doc_kw)
        if len(tt.split()) > 0 and tt not in orginal_kw_clean:
            orginal_kw_clean.append(tt)
    return orginal_kw_clean
#_______________________________________________
#orginal_kw = clean_orginal_kw(dtf['goldkeys'])

def get_exact_intersect(doc_orginal_kw, doc_my_kw):
    general = []
    for kw in doc_my_kw:
        for kww in doc_orginal_kw:
            if (kw == kww):
                #print("exact matching ========", kw, kww)
                if kww not in general:
                    general.append(kww)
    return general
#-----------------------------------------------------------------

def evaluate(top_N_keyphrases, references):
    ex = get_exact_intersect(references, top_N_keyphrases)
    try:
        P = (len(ex) / len(top_N_keyphrases))
    except ZeroDivisionError:
        P = 0
    try:
        R = (len(ex) / len(references))
    except ZeroDivisionError:
        R = 0
    F = (2 * P * R) / (P + R) if (P + R) > 0 else 0
    #print ('EXACT', len(ex))
    #print ('LEN_top_N_keyphrases', len(top_N_keyphrases))
    #print ('LEN_references', len(references))
    return (P, R, F)
################################################
def check_sent(word, total_sentences):
    sent_len = 0
    for sent in total_sentences:
        w_list = sent.split()
        if word in w_list:
            sent_len += 1     
    return int(sent_len)

def check_position_word_in_sent(word, total_sentences):
    for i in range(len(total_sentences)):
        w_list = total_sentences[i].split()
        if word in w_list:
            return i + 1
    return -1

def term_frequency(total_words):
    tf_score = {}
    for each_word in total_words:
        if each_word in tf_score:
            tf_score[each_word] += 1
        else:
            tf_score[each_word] = 1
    #Dividing
    tf_score.update((x, y/int(len(total_words))) for x, y in tf_score.items())
    return tf_score

def term_sent_frequency(total_words, total_sentences):
    tsf_score = {}
    for each_word in total_words:
        num_appear = check_sent(each_word, total_sentences)
        if num_appear > 0:
            tsf_score[each_word] = num_appear
        else:
            tsf_score[each_word] = 1
    tsf_score.update((x, y/len(total_sentences)) for x, y in tsf_score.items())
    return tsf_score

def inverse_sent_frequency(total_words, total_sentences):
    isf_score = {}
    for each_word in total_words:
        num_appear = check_sent(each_word, total_sentences)
        if num_appear > 0:
            isf_score[each_word] = num_appear
        else:
            isf_score[each_word] = 1
    #isf_score.update((x, y/len(total_sentences)) for x, y in isf_score.items())
    #isf_score.update((x, y/len(total_sentences)) for x, y in isf_score.items())
    isf_score.update((x, math.log(int(len(total_sentences))/y)) for x, y in isf_score.items())
    return isf_score

def term_position(total_words, total_sentences):
    tp_score = {}
    for each_word in total_words:
        pos_appear = check_position_word_in_sent(each_word, total_sentences)
        if pos_appear >= 1:
            tp_score[each_word] = pos_appear
        else:
            tp_score[each_word] = len(total_sentences)
    #isf_score.update((x, y/len(total_sentences)) for x, y in isf_score.items())
    #isf_score.update((x, y/len(total_sentences)) for x, y in isf_score.items())
    #print("TOTALWORD", total_words)
    #print("TOTALSENT", total_sentences)
    #print("score", tp_score)
    #tp_score.update((x, math.log(int(len(total_sentences))/y)) for x, y in tp_score.items())
    tp_score.update((x, 1 / y) for x, y in tp_score.items())
    return tp_score

def get_top_n(dict_elem, n):
    result = dict(sorted(dict_elem.items(), key = itemgetter(1), reverse = True)[:n])
    return result

def is_special_char(str):
    regex = re.compile('[@.+=!#$%^&*()<>?/\|}{~:\[\]]') 
    if(regex.search(str) == None): 
        return True
    else:
        return False

def containment_measure(string1, string2):
    lcs_score = 0
    string1 = string1.replace(' ', '')
    string2 = string2.replace(' ', '')
    len1 = len(string1)
    seq_match = difflib.SequenceMatcher(None, string1, string2) 
    match = seq_match.find_longest_match(0, len(string1), 0, len(string2))
    lcs_score = match.size / len1
    return lcs_score

def remove_key_substring(key_dict):
    idx1 = 0
    tmp_lcs = []
    for key1 in key_dict.keys():
        idx2 = 0
        for key2 in key_dict.keys():
            if idx1 != idx2:
                score = containment_measure(key1, key2)
                if score == 1.0 and len(key1) < 7:
                    tmp_lcs.append(key1)
            idx2 = idx2 + 1
        idx1 = idx1 + 1
    for k in tmp_lcs:
        key_dict[k] = 0
    return key_dict

def keyword_extraction(text, top):
    #Extract noun
    total_nouns = []
    total_sentences = []
    total_words = []
    blob = TextBlob(text)
    for noun in blob.noun_phrases:
        if (is_special_char(noun)):
            n = preprocess_text(noun)
            if len(n) >= 3:
                total_nouns.append(n)

    for w in total_nouns:
        n_underscore = w.replace(' ', '_')
        total_words.append(n_underscore)

    #Extract sentence
    for sents in blob.sentences:
        sents_new = preprocess_text(str(sents))
        for noun in total_nouns:
            n_underscore = noun.replace(' ', '_')
            sents_new = sents_new.replace(noun, n_underscore)
        total_sentences.append(sents_new)

    tf = term_frequency(total_words)
    tsf = term_sent_frequency(total_words, total_sentences)
    isf = inverse_sent_frequency(total_words, total_sentences)
    tp = term_position(total_words, total_sentences)

    score = {}
    for term in tf:
        num_term = len(term.split('_'))
        if num_term == 2:
            score[term] = tf.get(term)  * tsf.get(term) * isf.get(term) * tp.get(term) * math.log(math.sqrt(int(2+0.5)))
        elif num_term == 3:
            score[term] = tf.get(term)  * tsf.get(term) * isf.get(term)  * tp.get(term) * math.log(math.sqrt(int(3+0.5)))
        elif num_term == 4:
            score[term] = tf.get(term)  * tsf.get(term) * isf.get(term)  * tp.get(term) * math.log(math.sqrt(int(4+0.5)))
        else:
            score[term] = tf.get(term)  * tsf.get(term) * isf.get(term)  * tp.get(term) * math.log(math.sqrt(int(1+0.5)))
    score = remove_key_substring(score)
    return get_top_n(score, top)

def main():
    #500N-KPCrowd-v1.1
    #SemEval2010
    #Inspec
    #Nguyen2007
    #DUC2001
    path = "keyphrase-dataset/Inspec/"
    all_files = os.listdir(path+"docsutf8")
    all_keys = os.listdir(path+ "keys")
    for dirname, _, filenames in os.walk(path+"docsutf8"):
        for filename in filenames:
            print(os.path.join(dirname, filename))
    all_documents =[]
    all_keys = []
    all_files_names = []
    for i, fname in enumerate(all_files):
        with open(path+'docsutf8/'+fname, encoding='utf8') as f:
            lines = f.readlines()
        key_name = fname[:-4]
        with open(path+'keys/'+key_name+'.key') as f:
            k = f.readlines()
        all_text = ' '.join(lines)
        keyss = ' '.join(k)
        
        all_documents.append(all_text)
        all_keys.append(keyss.split("\n"))
        all_files_names.append(key_name)
    
    result_list = []
    #for i in range(1):
    for i in range(len(all_documents)):
        print("DOC_ID:", i)
        print("DOC_NAME:", all_files_names[i])
        keywords = keyword_extraction(all_documents[i], 5)
        kw_list = []
        for kw in keywords.keys():
            kw_list.append(kw.replace('_', ' '))
        
        references = clean_orginal_kw(all_keys[i])
        top_N_keyphrases = clean_orginal_kw(kw_list)

        print("Answer:", top_N_keyphrases)
        print("Gold:", references)
        print("==========================\n")
        
        result = evaluate(top_N_keyphrases, references)
        result_list.append(result)

    f1 = 0
    for tup in result_list:
        f = tup[2]
        f1 = f1 + f
    print("NumDoc", len(result_list))
    print("F1-Measure", f1 / len(result_list))

if __name__ == '__main__':
    main()
    #my_list1 = ["sawas dee", "Hello", "gmm"]
    #my_list2 = ["sawas dee", "Hello", "good"]
    #references = clean_orginal_kw(my_list1)
    #top_N_keyphrases = clean_orginal_kw(my_list2)
    #result = evaluate(top_N_keyphrases, references)
    #print(result)
    #print(preprocess_text("NLTK is a string graph-based mark with_friends processing library that takes strings as input."))
    text = """
Grids are inherently heterogeneous and dynamic. One important
problem in grid computing are resource selection, that is, finding
an appropriate resource set for the application.
""".replace('\n', ' ')