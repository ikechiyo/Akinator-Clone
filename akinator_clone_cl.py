# -*- coding: utf-8 -*-
import sys
import classification

def main():
    clf = classification.classification()

    #データファイルを読み込む
    clf.load()

##################################################
#ここから

#問題を出力
#print(clf.queation([0, 1, 2], [1, 3, 5]))

#回答を受け取る
#in@put()

#回答があるかどうかを調べる
#str = clf.answer([0, 1, 2], [1, 3, 5])
#もし～ならば(if, else, elsif)

#回答があったら出力してループを抜ける
#print

#回答がなかったら1に戻る
#～のあいだ(while, else)

#ここまで
##################################################
if __name__ == "__main__":
    sys.exit(int(main() or 0))
