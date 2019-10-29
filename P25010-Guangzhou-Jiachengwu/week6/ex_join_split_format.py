# 输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
words="one two three four"

# lwords=words.split()
#
# lwords.reverse()
#
# rewords=" ".join(lwords)
#
# print(rewords)
# print("{}".format(rewords))


def re_words(src):
    src2list=src.split()
    # 强行用一波format吧，不用就忘记了
    print("{}".format(" ".join(src2list[::-1])))

re_words(words)