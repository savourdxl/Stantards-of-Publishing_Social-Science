# based on titles
# didn't delete any words

from pprint import pprint
import pandas as pd
import os

import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel

import matplotlib.pyplot as plt

import pyLDAvis
import pyLDAvis.gensim_models as gensimvis

path = os.path.abspath(os.path.dirname(os.getcwd())) + '\\data'

info_article = pd.read_csv(path+'\\info\\info_article_o_8_n.csv')
info_issue = pd.read_csv(path+'\\info\\info_issue_o_8.csv')
info_year = pd.read_csv(path+'\\info\\info_year_o_8.csv')

titles_list = info_article['name_book_words'].values

titles_list_r = []

for i_title in titles_list:

    i_title = eval(i_title)

    i_title_r = []
    for i_i_title in i_title:
        if i_i_title != None:
            i_title_r.append(i_i_title)

    titles_list_r.append(i_title_r)

titles_dict = corpora.Dictionary(titles_list_r)

corpus = [titles_dict.doc2bow(i_keyword) for i_keyword in titles_list_r]


def compute_coherence_values(corpus_r, list_r, dictionary,
                             start = 10, end=20, step=2):

    coherence_values = []
    model_list = []

    for num_topics in range(start,end,step):
        model = gensim.models.LdaMulticore(corpus=corpus_r,
                                           id2word=dictionary,
                                           num_topics=num_topics,
                                           random_state=0)
        model_list.append(model)

        coherence_model = CoherenceModel(model=model,
                                         texts=list_r,
                                         dictionary=dictionary,
                                         coherence='c_v')
        coherence_values.append(coherence_model.get_coherence())

    return model_list, coherence_values


model_list, coherence_values = compute_coherence_values(corpus_r=corpus,
                                                        list_r= titles_list_r,
                                                        dictionary=titles_dict,
                                                        start=2, end=80, step=1)

plt.close()
x = range(2,80,1)
plt.plot(x, coherence_values)
plt.xlabel("Number of Topics")
plt.ylabel("Coherence score")
plt.savefig(path+'\\picture\\coherence_score_2.png')

# max(coherence_values)
# 0.5225033865750524
# coherence_values.index(max(coherence_values))  34
# number of topics : 36

lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       id2word=titles_dict,
                                       num_topics=36,
                                       random_state=0)

pprint(lda_model.print_topics())

my_pic = gensimvis.prepare(lda_model, corpus, titles_dict)

pyLDAvis.save_html(my_pic, path+'\\picture\\lda_2.html')

# the result doesn't went well
