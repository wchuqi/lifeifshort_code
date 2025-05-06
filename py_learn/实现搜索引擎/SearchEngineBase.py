'''
SearchEngineBase 可以被继承，继承的类分别代表不同的算法引擎。

每一个引擎都应该实现 process_corpus() 和 search() 两个函数，对应我们刚刚提到的索引器和检索器。

main()函数提供搜索器和用户接口，于是一个简单的包装界面就有了。

add_corpus() 函数负责读取文件内容，将文件路径作为 ID，连同内容一起送到process_corpus 中。

process_corpus 需要对内容进行处理，然后文件路径为 ID ，将处理后的内容存下来。

处理后的内容，就叫做索引（index）。

search 则给定一个询问，处理询问，再通过索引检索，然后返回
'''
class SearchEngineBase(object):
    def __init__(self):
        pass
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
            self.process_corpus(file_path, text)
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')
    def search(self, query):
        raise Exception('search not implemented.')

def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)
    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)