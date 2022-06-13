import nltk 
from nltk.book import *
from nltk import re
from nltk import word_tokenize
#1. Cuál es el número de tokens en	Moby Dick?
mysent_tokens_nopunct = [word for word in word tokenize(mysent)	if re.search("\w",	word)]
numero_tokens = len(moby_dick_tokens_nopunct)
# output 218621
# 1. Cuál es el número de types en	Moby Dick?
numero_types = len(set(moby_dick_tokens_nopunct))
# output 17140
# Token ratio moby dick:
moby_dick_token_ratio = numero_types / numero_tokens
# output 0.07840051962071347
# Token ratio wsj
wsj_tokens_nopunct = [word.lower() for word in wsj_tokens if re.search("\w", word)]
numero_tokens_wsj = len(wsj_tokens_nopunct)
numero_types_wsj = len(set(wsj_tokens_nopunct))
wsj_token_ratio = numero_types_wsj / numero_tokens_wsj
wsj_token_ratio
# output  0.129748424801388
# 5. Cuál de los dos tiene más diversidad	léxica?	
# Como el ratio de WSJ es mayor, podemos decir que es más diverso en palabras 
# 6. Puede	pensar una razón por por la cual ese corpus es más diverso que el otro?
# Al tener un menor tamaño es probable que tengamos menor cantidad de palabras repetidas, además el corpus de un libro es distinto al de un diario el cual no necesita un contexto común para cada noticia
# 7.	Cual	es el	“Maximum	Likelikhood	Estimate	(MLE)” de	la	palabra	“whale” (ballena)	en	Moby	Dick?	
moby_dick_whale_occurrences = moby_dick_tokens_nopunct.count("whale")
moby_dick_whale_occurrences
# output 1226
whale_mle = moby_dick_whale_occurrences / numero_tokens
whale_mle
# output 0.005607878474620462
wsj_whale_occurrences = wsj_tokens_nopunct.count("whale")
whale_mle_wsj  = wsj_whale_occurrences / numero_tokens_wsj
whale_mle_wsj
# output 0.0

