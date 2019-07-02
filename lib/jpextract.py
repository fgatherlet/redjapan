import MeCab
import re
mecab = MeCab.Tagger("-d /opt/local/lib/mecab/dic/mecab-ipadic-neologd")

def extract_noun(text):
    result = []
    node = mecab.parseToNode(text)
    while node:
        surface = node.surface
        feature = node.feature
        node = node.next
        m = re.match("^名詞", feature)
        if m:
            result.append(surface)
    return result

