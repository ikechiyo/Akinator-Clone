# -*- coding: utf-8 -*-
import sys
import classification

def main():
    clf = classification.classification()

    #データファイルを読み込む
    clf.load()

##################################################
#ここから

    #答えが解ったら人の名前、解らなかったら空文字
    print(clf.answer([0, 1, 2], [1, 3, 5]))

     #問題が返ってくる
    print(clf.queation([0, 1, 2], [1, 3, 5]))

#ここまで
##################################################
if __name__ == "__main__":
    sys.exit(int(main() or 0))
