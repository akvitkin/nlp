nltk.help.upenn_tagset(".*")
from nltk.corpus import treebank
treebank.fileids()
treebank.tagged_words("wsj_0001.mrg")[0:]
race1 = nltk.tag.str2tuple('race/NN')
race1
# output ('race', 'NN')
race2 = nltk.tag.str2tuple('race/VB')
race2
# output ('race', 'VB')
from nltk.corpus import brown
len(brown.tagged_words())
# output 1161192
brown.tagged_words().count(race1)
# output 94
brown.tagged_words().count(race2)
# output 4
from nltk.corpus import brown
unigram_tagger = nltk.tag.UnigramTagger(brown.tagged_sents(categories='news')[:5000])
unigram_tagger
# output <UnigramTagger: size=14394>
from nltk import word_tokenize
S = "The Secretariat is expected to race tomorrow."
unigram_tagger.tag(S_tok)
# output 
#  [('The', 'AT'),
#  ('Secretariat', 'NN-TL'),
#  ('is', 'BEZ'),
#  ('expected', 'VBN'),
#  ('to', 'TO'),
#  ('race', 'NN'),
#  ('tomorrow', 'NR'),
#  ('.', '.')]
hmm_tagger.tag(S_tok)
# output 
# [('The', 'AT'),
#  ('Secretariat', 'NN-TL'),
#  ('is', 'BEZ'),
#  ('expected', 'VBN'),
#  ('to', 'TO'),
#  ('race', 'VB'),
#  ('tomorrow', 'NR'),
#  ('.', '.')]
# race es verbo

# Sentencia ambigua inventada
sentence = "give me a ring later"
sentence_token =   word_tokenize(sentence)
unigram_tagger.tag(sentence_token)
# output [('give', 'VB'), ('me', 'PPO'), ('a', 'AT'), ('ring', 'NN'), ('later', 'RBR')]
hmm_tagger.tag(sentence_token)
# output [('give', 'VB'), ('me', 'PPO'), ('a', 'AT'), ('ring', 'NN'), ('later', 'RBR')]
titular = "Juvenile Court to Try Shooting Defendant"
titular_token =   word_tokenize(titular)
titular_token
# output 
# [('Juvenile', 'JJ-TL'),
#  ('Court', 'NN-TL'),
#  ('to', 'IN'),
#  ('Try', 'AT'),
#  ('Shooting', 'AT'),
#  ('Defendant', 'AT')]
Defendant1 = nltk.tag.str2tuple('Defendant/NN')
Defendant1
# output ('Defendant', 'NN')
