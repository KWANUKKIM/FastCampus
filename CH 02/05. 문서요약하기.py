"""
Anaconda Prompt
>conda activate FastCampus
>pip install gensim==3.7.3
>pip list
>https://github.com/Kyubyong/wordvectors
"""

import gensim
model = gensim.models.Word2Vec.load('ko/ko.bin')
model.wv.most_similar("뉴스")
"""
model.wv.similarity('자동차', '강아지')
model.wv.similarity('자동차', '버스')
"""