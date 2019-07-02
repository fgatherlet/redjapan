import MeCab

# echo `mecab-config --dicdir`/mecab-ipadic-neologd
# /opt/local/lib/mecab/dic/mecab-ipadic-neologd
mecab = MeCab.Tagger("-d /opt/local/lib/mecab/dic/mecab-ipadic-neologd")
text = "よつばととは、なんだったのか。漫画作品として優れている。"
node = mecab.parseToNode(text)
while node:
    surface = node.surface
    feature = node.feature
    print(surface)
    print(feature)
    node = node.next
