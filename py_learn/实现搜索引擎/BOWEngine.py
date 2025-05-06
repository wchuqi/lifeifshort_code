'''
应该怎么优化呢？

最直接的一个想法，就是把语料分词，看成一个个的词汇，这样就只需要对每篇文章存储它所有词汇的 set 即可。

根据齐夫定律（Zipf’s law，https://en.wikipedia.org/wiki/Zipf%27s_law），在自然语言的语料库里，一个单词出现的频率与它在频率表里的排名成反比，呈现幂律分布。

因此，语料分词的做法可以大大提升我们的存储和搜索效率。

Bag of Words 和 Inverted Index

BOW Model，即 Bag of Words Model，中文叫做词袋模型。这是 NLP 领域最常见最简单的模型之一。

假设一个文本，不考虑语法、句法、段落，也不考虑词汇出现的顺序，只将这个文本看成这些词汇的集合。
于是相应的，我们把 id_to_texts 替换成 id_to_words，这样就只需要存这些单词，而不是全部文章，也不需要考虑顺序。

其中，process_corpus() 函数调用类静态函数 parse_text_to_words，将文章打碎形成词袋，放入 set 之后再放到字典中。

search() 函数则稍微复杂一些。这里我们假设，想得到的结果，是所有的搜索关键词都要出现在同一篇文章中。

那么，我们需要同样打碎 query 得到一个 set，然后把 set 中的每一个词，和我们的索引中每一篇文章进行核对，看一下要找的词是否在其中。
而这个过程由静态函数 query_match 负责。


'''

import re

from 实现搜索引擎.SearchEngineBase import SearchEngineBase, main


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}
    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)
    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_words.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results
    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True
    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w ]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)

search_engine = BOWEngine()
main(search_engine)