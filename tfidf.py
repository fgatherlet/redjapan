#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


def main():
    # データフレームを表示するときカラムを省略しない
    pd.set_option('display.max_columns', None)
    # 浮動小数点を表示するときは小数点以下 2 桁で揃える
    pd.options.display.float_format = '{:0.2f}'.format

    # 取り扱うコーパス
    corpus = [
        'This is the first document.',
        'This document is the second document.',
        'And this is the third one.',
        'Is this the first document?',
    ]

    # 単語の数をカウントする
    count_vectorizer = CountVectorizer()
    X_count = count_vectorizer.fit_transform(corpus)

    # 見やすさのために表示するときは pandas のデータフレームにする
    df = pd.DataFrame(data=X_count.toarray(),
                      columns=count_vectorizer.get_feature_names())
    print('--- BoW (Bag of Words) ---')
    print(df)

    # scikit-learn の TF-IDF 実装
    tfidf_vectorizer = TfidfVectorizer()
    X_tfidf = tfidf_vectorizer.fit_transform(corpus)

    # IDF を表示する
    print('--- IDF (Inverse Document Frequency) ---')
    df = pd.DataFrame(data=[tfidf_vectorizer.idf_],
                      columns=tfidf_vectorizer.get_feature_names())
    print(df)

    # TF-IDF を表示する
    print('--- TF-IDF ---')
    df = pd.DataFrame(data=X_tfidf.toarray(),
                      columns=tfidf_vectorizer.get_feature_names())
    print(df)


if __name__ == '__main__':
    main()
