import string
from nltk.tokenize import word_tokenize
import re
import pickle
from nltk.stem import WordNetLemmatizer
from collections import Counter
import pandas as pd
import os

DS_STORE = '.DS_Store'
CLEAN_FILINGS_PATH = 'data/sec-edgar-filings-cleaned'
lemmatizer = WordNetLemmatizer()


def save_pkl(obj, path):
    """
    Save an object to path.
    """
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


def load_pkl(path):
    """
    Load a pickle from path.
    """
    with open(path, 'rb') as f:
        return pickle.load(f)


STOPWORDS = load_pkl('data/stopwords.pkl')


def df_from_filings():
    filings_cik_cleaned = os.listdir(CLEAN_FILINGS_PATH)
    if DS_STORE in filings_cik_cleaned: filings_cik_cleaned.remove(DS_STORE)

    data = []

    for i, cik in enumerate(sorted(filings_cik_cleaned)):  # all fillings
        path_cik = f'{CLEAN_FILINGS_PATH}/{str(cik)}'
        report_type = os.listdir(path_cik)
        if DS_STORE in report_type: report_type.remove(DS_STORE)

        for rt in report_type:  # N-CSR and N-CSRS
            path_report_type = path_cik + '/' + str(rt)
            report_folder = os.listdir(path_report_type)
            if DS_STORE in report_folder: report_folder.remove(DS_STORE)

            for rf in report_folder:  # report identity
                path_report_folder = path_report_type + '/' + rf
                filling = os.listdir(path_report_folder)

                for file in filling:  # file submission text
                    path_file = path_report_folder + '/' + str(file)
                    with open(path_file, 'r') as f:
                        txt = f.read()
                    # print(path_file)
                    data.append((cik, rt, rf, file, txt))
    return pd.DataFrame(data, columns=['cik', 'report_type', 'report_identity', 'file', 'text'])


def clean_punctuation(text):
    # First, for each of the following characters (or symbols), the function replaces it by an empty space on the text
    for a_sign in ['\\n', '\\t', '☐', '☒', '\xa0', '●', '“', '”']:
        text = text.replace(a_sign, " ")

    # Here, for each punctution in a set of all existing punctuations, the function also replaces it by an empty space.
    for a_punc in string.punctuation:
        text = text.replace(a_punc, " ")

    # Morever, the fuction replaces '\s+' (which represents a sequence of empty spaces) by an single empty space, avoiding unecessary spaces
    # and also sets all letters to lower case to make it easier to analyse later.

    text = re.sub('\s+', " ", text).lower()

    return text.strip()

    # Very important: This function here is for exposition only. It will be modified later in section 5 when we start using
    # the dictionary of negative words.

    # Tokenizing and counting the total frequency of words


def word_count(text):
    word_list = word_tokenize(text)  # splits the text into words and assigns it to a new list
    total_num = len(word_list)  # count the number of words in the new list
    return total_num, word_list


def remove_stopwords(text, stopwords):
    result_words = [word for word in text.split() if word.lower() not in stopwords]
    result = ' '.join(result_words)
    return result


def lemmatize(str):
    lemmatizer.lemmatize(str, pos="a")


def remove_frequent(text, nb_removals_max=250, min_occurrences=50):
    cnt = Counter()
    for word in text.split():
        cnt[word] += 1
    freq = set([w for (w, wc) in cnt.most_common(nb_removals_max) if wc > min_occurrences])
    return " ".join([word for word in text.split() if word not in freq])


def preprocess(text):
    #     ls=LancasterStemmer()
    #     lm = WordNetLemmatizer()

    text = remove_stopwords(text, STOPWORDS)
    text = clean_punctuation(text)
    text = remove_frequent(text)
    return text
