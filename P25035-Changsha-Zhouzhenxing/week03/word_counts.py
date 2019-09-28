# 任一个英文的纯文本文件，统计其中的单词出现的个数


def word_counts(file, word):
    '''
    :param file: 要搜索的文本文件
    :param word: 要搜索的单词
    :return: 返回单词在文本文件中出现的次数
    '''
    qty = 0     #word在每行中出现的次数
    total = 0   #word在file中出现的总次数

    with open(file, encoding="utf-8") as file:
        while True:
            str = file.readline()
            if str == '':
                break

            qty = str.count(word)
            total += qty

    return total


if __name__ == '__main__':
    file = r".\Python之禅.txt"
    word = "better"
    print("“"+ word + "”" , "在文件 “" , file.replace(".\\", '') , "”中出现的次数为：" , word_counts(file, word))
