# -*- coding: utf-8 -*-
import sys
import classification

def main():
    clf = classification.classification()

    #データファイルを読み込む
    clf.load()

#    while True:
#        str = input()
#        print(str)
#        if str == "1":
#            break



##################################################
#ここから

#問題を出力
#print(clf.queation([0, 1, 2], [1, 3, 5]))
    while True:
        print("ーーーーーーーーーーーーーーーーーーーー")
        print(clf.queation([0, 1, 2], [1, 3, 5]))
        print("￣￣￣￣￣￣￣￣￣∨￣￣￣￣￣￣￣￣￣￣")
        print("　　　　　　　　∧_∧")
        print("　　　　　　　 < ｀∀´>　")
        print("　　　　　　　　(　∽) ")
        print("　　　　　　　  )ノ")
        print("　　　　　　　　（_　")
        print("　　　　　　　[il=li]　")
        print("　　　　　　　　)=(_") 
        print("　　　　　　　(-==-)") 
        print("　　　　　　　 `ｰ‐'' ") 
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓") 
        print("┃ 「YES」なら 5 、「NO」なら 1	┃")
        print("┃ 「わからない場合」は 0 を入力 ┃") 
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛") 


#回答を受け取る
#input()
        str = input()
        answer = clf.answer([0, 1, 2], [1, 3, 5])

#回答があるかどうかを調べる
#str = clf.answer([0, 1, 2], [1, 3, 5])
#もし～ならば(if, else, elsif)

        if answer == "":
            pass
        else:
            print("＿人人人人人人＿") 
            print(answer)
            print("￣Y^Y^Y^Y^Y^Y￣") 
            break

#回答があったら出力してループを抜ける
#print


#回答がなかったら1に戻る
#～のあいだ(while, else)


#ここまで
##################################################
if __name__ == "__main__":
    sys.exit(int(main() or 0))
