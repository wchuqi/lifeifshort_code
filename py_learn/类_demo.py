class Document():
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context # __ 开头的属性是私有属性
    def get_context_length(self):
        return len(self.__context)
    def intercept_context(self, length):
        self.__context = self.__context[:length]
harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '... Forever Do not believ')

print(harry_potter_book.title)
print(harry_potter_book.author)
print(harry_potter_book.get_context_length())

harry_potter_book.intercept_context(10)
print(harry_potter_book.get_context_length())

#print(harry_potter_book.__context)
# AttributeError: 'Document' object has no attribute '__context'

class Document():
    # 类常量
    WELCOME_STR = 'Welcome! The context for this book is {}.'
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context
    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')
    # 成员函数
    def get_context_length(self):
        return len(self.__context)
    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)

empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'P')
print(empty_book.get_context_length())
print(empty_book.get_welcome('indeed nothing'))


class Entity():
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type
    def get_context_length(self):
        raise Exception('get_context_length not implemented')
    def print_title(self):
        print(self.title)
class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        Entity.__init__(self, 'document')
        self.title = title
        self.author = author
        self.__context = context
    def get_context_length(self):
        return len(self.__context)

class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'video')
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return self.__video_length

harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling', '... Forever Do not')
harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)

print(harry_potter_book.object_type)
print(harry_potter_movie.object_type)

harry_potter_book.print_title()
harry_potter_movie.print_title()

print(harry_potter_book.get_context_length())
print(harry_potter_movie.get_context_length())