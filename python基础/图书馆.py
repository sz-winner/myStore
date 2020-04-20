# 主要功能：
# 1. 查询书籍：可以一键查询系统里所有书籍的基本信息和借阅状态。
# 2. 添加书籍：往系统添加书籍时，需要输入书籍的基本信息（书号、书名、作家、出版社、语言、推荐语），记录献书人、献书日期。
# 3. 借阅书籍：当书籍的借阅状态是“未借出”的时候，书籍才可以出借，借出后状态变成“已借出”，记录借书人和借出日期。
# 4. 归还书籍：归还成功后书籍的借阅状态会更改成“未借出”，记录归还日期，可再次被借阅。
# 5. 记录书籍借阅次数：书籍没被借阅一次，借阅计数器自动+1.
# 6. 读者信息：记录读者编号、姓名、电话号码、登记日期
# 7. 主要对象：书籍Book，读者Reader，管理员 BookManger


class Book:

    def __init__(self, name, author, comment, state=0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state

    def __str__(self):
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)


class BookManager:

    books = []

    def __init__(self):
        book1 = Book('惶然录', '费尔南多·佩索阿', '一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅', '简媜', '调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手', '卡森·麦卡勒斯', '我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)

    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            else:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。')
                break

    def show_all_book(self):
        print('书籍信息如下：')
        for book in self.books:
            print(book)
            print('')

    def show_author_book(self):
        author = input('请输入想查询作家的名称：')
        if author in self.authors:  # 判断寻找的作者在不在作者列表中，如果在，进行下一步
            print(author + '的作品有：')
            for book in self.books:  # 遍历书籍列表，这个语句将book实例化
                if book.author == author:  # 如果书的作者与输入的作者相同，进行下一步
                    print(book)  # 打印书籍的信息
        else:
            print('很可惜，我们暂时没有收录这位作者的作品')

    def add_book(self):
        new_name = input('请输入书籍名称：')
        new_author = input('请输入作者名称：')
        new_comment = input('请输入书籍推荐语：')
        new_book = Book(new_name, new_author, new_comment)
        self.books.append(new_book)
        print('书籍录入成功！\n')

    def check_book(self, name):
        for book in self.books:
            if book.name == name:
                return book
        else:
            return None

    def lend_book(self):
        name = input('请输入书籍的名称：')
        res = self.check_book(name)

        if res !=None:
            if res.state == 1:
                print('你来晚了一步，这本书已经被借走了噢')
            else:
                print('借阅成功，借了不看会变胖噢～')
                res.state = 1
        else:
            print('这本书暂时没有收录在系统里呢')

    def return_book(self):
        name = input('请输入归还书籍的名称：')
        res = self.check_book(name)
        if res==None:
            print('没有这本书噢，你恐怕输错了书名～')
        else:
            if res.state == 0:
                print('这本书没有被借走，在等待有缘人的垂青呢！')
            else:
                print('归还成功！')
                res.state = 0


manager = BookManager()
manager.menu()
